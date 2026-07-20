import random
num=random.randint(1,10)

guess_number1=int(input("请输入第一次要猜测的数字："))
if guess_number1>num:
    print("不好意思，猜大了哦，再猜一次吧")
    guess_number2=int(input("请输入第二次要猜测的数字"))
    if guess_number2>num:
        print("不好意思，猜大了哦，再猜最后一次吧")
        guess_number3=int(input("请输入第三次要猜测的数字"))
        if guess_number3!=num:
            print("不好意思，还是猜错了，正确答案是%d"%num)
        else:
            print("恭喜你第三次猜对了")
    elif guess_number2<num:
        print("不好意思，猜小了哦，再猜最后一次吧")
        guess_number3 = int(input("请输入第三次要猜测的数字"))
        if guess_number3!=num:
            print("不好意思，还是猜错了，正确答案是%d"%num)
        else:
            print("恭喜你第三次猜对了")
    else:
        print("恭喜你第二次猜对了")

elif guess_number1<num:
    print("不好意思，猜小了哦，再猜一次吧")
    guess_number2 = int(input("请输入第二次要猜测的数字"))
    if guess_number2>num:
        print("不好意思，猜大了哦，再猜最后一次吧")
        guess_number3=int(input("请输入第三次要猜测的数字"))
        if guess_number3!=num:
            print("不好意思，还是猜错了，正确答案是%d"%num)
        else:
            print("恭喜你第三次猜对了")
    elif guess_number2<num:
        print("不好意思，猜小了哦，再猜最后一次吧")
        guess_number3 = int(input("请输入第三次要猜测的数字"))
        if guess_number3!=num:
            print("不好意思，还是猜错了，正确答案是%d"%num)
        else:
            print("恭喜你第三次猜对了")
    else:
        print("恭喜你第二次猜对了")
else:
    print("恭喜你第一次就猜对了")