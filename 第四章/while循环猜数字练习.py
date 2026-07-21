"""
用while设计猜数字
"""
import random
num=random.randint(1,100)
#定义一个变量记录猜测次数
count=0

#通过布尔类型本身做循环的条件
flag=True
while flag:
    guess_number=int(input("请输入你猜测的数字:"))
    count+=1
    if guess_number!=num:
       if guess_number>num:
        print("不好意思，猜大了")
       else:
        print("不好意思，猜小了")
    else:
        print("恭喜你猜中了")
        #用False本身做终止条件
        flag=False

print(f"你总共猜测了{count}次")