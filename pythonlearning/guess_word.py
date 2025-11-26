correct_word = input('输入要猜的单词：')

guess_word = ''

max_guesses = len(correct_word) * 2

char_index = 0
while guess_word != correct_word and max_guesses > 0:
    print(f'还有{max_guesses}次机会')
    char = input(f'猜第{char_index+1}个字母：')
    if char == correct_word[char_index]:
        guess_word += char
        print('此字母正确！')
        char_index += 1
    else:
        print('此字母错误！')

    max_guesses -= 1

if guess_word == correct_word:
    print('恭喜你，猜对了！')
else:
    print('游戏结束！')
