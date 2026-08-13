"""
演示tuple元组的定义和操作
"""
#定义元组
t1=(1,"Hello",True)
t2=()
t3=tuple()
print(f"t1的类型是：{type(t1)}，内容是：{t1}")
print(f"t2的类型是：{type(t2)}，内容是：{t2}")
print(f"t3的类型是：{type(t3)}，内容是：{t3}")

#定义单个元素的元组
t4=("hello",)     #只有单个元素的元组必须要在该元素后加个逗号
print(f"t4的类型是：{type(t4)}，内容是：{t4}")

#元组的嵌套
t5=((1,2,3),(4,5,6))
print(f"t5的类型是：{type(t5)}，内容是：{t5}")

#下标索引去取出内容
num=t5[1][2]
print(f"从嵌套元组中取出的数据是：{num}")

#元组的操作：index查找方法
t6=("lyh","math","python")
index=t6.index("math")
print(f"在元组t6中查找math的下标是：{index}")
#元组的操作：count统计方法
t7=("lyh","math","math","math","python")
num=t7.count("math")
print(f"在元组t7中统计math的数量有{num}个")
#元组的操作：len函数统计元组元素数量
t8=("lyh","math","math","math","python")
num=len(t8)
print(f"t8元组中的元素有{num}个")

#元组的遍历：while
index=0
while index<len(t8):
    print(f"t8元组的元素有：{t8[index]}")
    index+=1
#元组的遍历：for
for element in t8:
    print(f"2t8元组的元素有：{element}")

#元组和列表区别是元组本身不可以修改，但对于特殊的元组可以改
t9=(1,2,["math","python"])  #该元组元素里有list所以我们可以改list的内容来间接改元组
print(f"t9的内容是{t9}")
t9[2][1]="编程"
t9[2][0]="数学"
print(f"t9的内容是{t9}")