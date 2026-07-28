"""
演示函数参数使用
"""

def add(a,b):
    result=a+b
    print(f"{a} + {b} = {result}")

add(1,2)


#练习案例：查核酸
def tem(x):
    if x<=37.5:
        print(f"体温测量中，您的体温是：{x}度，体温正常请进。")
    else:
        print(f"体温测量中，您的体温是：{x}度，需要隔离！")

tem(37.6)