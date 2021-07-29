import random

Hangman_list = []
text = open("D:\\PyFile\\pythonProject\\test\\Hangman.txt")  # 导入文件
while True:
    word = text.readline()
    if not word:
        break

    word = word.strip("\n")
    Hangman_list.append(word)

number = random.randint(0, 274926)
word_length = len(Hangman_list[number])  # 生成随机单词
unknown = "_" * word_length

life_number = 7

while life_number > 0 and unknown != Hangman_list[number]:
    print("*" * 50)
    print("")
    print(unknown)
    print("you can guess now, please choose from the 26 letters")
    guess = input("guess letter: ")
    flag = False
    count = 0
    for letter in Hangman_list[number]:
        if letter == guess:
            string = list(unknown)
            string[count] = guess
            unknown = ''.join(string)  # 列表与字符串的转换
            count += 1
            flag = True
        else:
            count += 1
    if flag:
        print("you get one right number. you have %d chances left" % life_number)
        print()
        print("*" * 50)
    else:
        life_number = life_number - 1
        print("the letter is wrong. you have %d chances left" % life_number)
        print("")
        print("*" * 50)
        # 循环进行猜测
if Hangman_list[number] == unknown:
    print("haha, you win, congratulation!")
    print("")
else:
    print("Oh, you are hanged!!!")
    print("")

print("the final word is: ", Hangman_list[number])  # 提示最终的单词
text.close()
