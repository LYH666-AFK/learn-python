"""
演示range()语句的基础使用
"""

#3个语法取值范围都是左闭右开，step可以理解为公差，不输入step默认是1
#语法1 range()
for x in range(10):
    print(x)

#语法2 range(num1,num2)
for i in range(5,10):
    print(i)

#语法3 range(num1,num2,step)
for j in range(5,10,2):
    print(j)


#练习
num=101
count=0
for x in range(2,num,2):
    count += 1
print(f"1到100内有{count}个偶数。")