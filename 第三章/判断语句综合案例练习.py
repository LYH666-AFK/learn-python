#自己手打的复杂版（思路一）
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


#答案的简单版（思路二）
import random
num=random.randint(1,10)

guess_number1=int(input("输入你要猜测的数字："))
if guess_number1==num:
    print("恭喜，第一次就猜中了")
else:
    if guess_number1>num:
        print("你猜测的数字大了")
    else:
        print("你猜测的数字小了")

    guess_number2=int(input("再次输入你要猜测的数字："))

    if guess_number2==num:
        print("恭喜，第二次猜中了")
    else:
        if guess_number2>num:
            print("你猜测的数字大了")
        else:
            print("你猜测的数字小了")

        guess_number3=int(input("第三次输入你要猜测的数字："))

        if guess_number3==num:
            print("第三次猜中了")
        else:
            print("三次机会用完了，没有猜中。")