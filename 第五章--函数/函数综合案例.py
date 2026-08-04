"""
函数综合案例
"""
money=5000000
#name=None  这行可不写，只为方便回忆None
name=input("请输入您的姓名：")

def menu():
    print("---------------主菜单---------------")
    print(f"{name}，您好，欢迎来到银行ATM。请选择操作：")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return input("请输入您的选择：")

def inquiry(show_header):
    if show_header:
        print("---------------查询余额---------------")
    print(f"{name}，您好，您的余额剩余：{money}元")

def deposit(num):
    global money
    money+=num
    print("---------------存款---------------")
    print(f"{name}，您好，您存款{num}成功")
    inquiry(False)

def withdraw(num):
    global money
    money-=num
    print("---------------取款---------------")
    print(f"{name}，您好，您取款{num}成功")
    inquiry(False)

while True:
    keyboard_input=menu()
    if keyboard_input== "1":
        inquiry(True)
        continue
    elif keyboard_input== "2":
        num=int(input("请输入您想要存入的金额："))
        deposit(num)
        continue
    elif keyboard_input== "3":
        num=int(input("请输入您想要取出的金额："))
        withdraw(num)
        continue
    else:
        print("程序退出了")
        break