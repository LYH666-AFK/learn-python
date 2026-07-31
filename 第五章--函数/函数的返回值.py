"""
演示：定义函数返回值的语法格式
"""

#定义一个函数，完成两数相加功能
def add(a,b):
    result = a+b
    #通过返回值，将相加的结果返回给调用者
    return result

#函数的返回值通过变量去接收
r=add(5,6)
print(r)


#演示特殊字面量：None
#无return的语句的函数返回值
def say_hi():
    print("你好呀")
result = say_hi()
print(f"无返回值函数，返回的内容是：{result}")
print(f"无返回值函数，返回的内容类型是：{type(result)}")


#主动返回None的函数
def say_hi2():
    print("你好呀")
    return None

result = say_hi2()
print(f"无返回值函数，返回的内容是：{result}")
print(f"无返回值函数，返回的内容类型是：{type(result)}")


#None用于if判断
def check_age(age):
    if age > 18:
        return "SUCCESS"
    else:
        return None

result = check_age(16)
if not result:
    #进入if表示result是None值 也就是False
    print("未成年，不可以进入")


#None用于声明无初始内容的变量
name=None