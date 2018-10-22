import random

num = random.randint(1,100000)
one = "I'm thinking of a number! Try to guess the number,You are thinking of:"
print(one, end="")
while 1:
    guessNumber = input()
    if guessNumber is not None:
        if guessNumber.isdigit():
            # isdigit 判断输入是否全部为数字
            guessNumber = int(guessNumber)
            if guessNumber > num:
                print("too high! Guess again:")
            elif guessNumber < num:
                print("too low! Guess again:")
            else:
                print("That's it! You're smart")
                break
        else:
            print('please input numbers')
input("点击 enter 键退出")
