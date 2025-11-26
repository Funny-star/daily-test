import os


class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True


class Library():
    def __init__(self):
        self.book_list: list[Book] = []

    def add_book(self, title, author):
        # 检查库中是否已有此书
        for book in self.book_list:
            if book.title == title and book.author == author:
                # 已借出：归还
                # 未借出：提示并返回
                if book.is_available:
                    print('书已入库')
                    return
                else:
                    book.is_available = True
                    print('还书成功')
                    return

        # 存书
        new_book = Book(title, author)
        self.book_list.append(new_book)
        print('入库成功')

        # new_book = Book(title, author)

        # if len(self.book_list) == 0:
        #     self.book_list.append(new_book)
        #     print('入库成功')

        # else:
        #     for book in self.book_list:
        #         if book.title == new_book.title and book.is_available == False:
        #             book.is_available = True
        #             print('还书成功')
        #             break
        #         elif book.title == new_book.title and book.is_available == True:
        #             print('书已入库')
        #             break
        #         else:
        #             self.book_list.append(new_book)
        #             print('入库成功')
        #             break

    def lend_book(self, title):
        for book in self.book_list:
            if book.title == title and book.is_available == True:
                book.is_available = False
                print('借阅成功')
            elif book.title == title and book.is_available == False:
                print('以借用')
            else:
                print('库存无此书')

    def print_book_list(self):
        if len(self.book_list) == 0:
            print('none book')
        for book in self.book_list:
            if book.is_available == True:
                print(f'书名：{book.title} 作者：{book.author} ', end='\n')

        pass


def library_body():
    library = Library()
    while True:
        key = input('按a加入图书/按l借书/按p查询书单:')
        os.system('cls')

        if key == 'a':
            title = input('请输入添加书的名字：')
            author = input('请输入添加的书的作者：')
            library.add_book(title, author)

        elif key == 'l':
            if len(library.book_list) == 0:
                print('库中无书')
                continue
            title = input('请输入你要借的书的名字：')
            library.lend_book(title)

        elif key == 'p':
            library.print_book_list()


library_body()
