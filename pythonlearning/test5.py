word = input('输入要猜的单词：')

a = 0

word_2 = ""

for i in range(1, 2*len(word)+1):
    print(f'还有{2*len(word)-i+1}次机会')
    b = input(f'猜第{a+1}个字母：')
    if b == word[a]:
        a += 1
        word_2 = word_2[:a] + word[a-1] + word_2[a:]
        print(word_2)
        if word_2 == word:
            break

a = 0

print('猜对了')
