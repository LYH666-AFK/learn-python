"""
演示数据容器之：list列表的常用操作
"""
from fontTools.merge.util import first

mylist=["lyh","math","python"]
#1.1 查找某元素在列表内的下标索引
index=mylist.index("lyh")
print(f"lyh在列表中的下标索引值是：{index}")
#1.2如果被查找的元素不存在，会报错

#2. 修改特定下标索引的值
mylist[0]="LYH"
print(f"列表被修改元素值后，结果是：{mylist}")

#3. 在指定下标位置插入新元素
mylist.insert(1,"best")
print(f"列表插入元素后，结果是：{mylist}")

#4. 在列表的尾部追加'''单个'''新元素
mylist.append("first")
print(f"列表在追加了元素后，结果是：{mylist}")

#5. 在列表的尾部追加'''一批'''新元素
mylist2=[1,2,3]
mylist.extend(mylist2)
print(f"列表在追加了一个新的列表后，结果是：{mylist}")

#6. 删除指定下标索引的元素（2种方式）
mylist=[1,2,3]
#6.1 方式1：del 列表[下标]
del mylist[2]
print(f"列表删除元素后，结果是：{mylist}")
#6.2 方式2：列表.pop(下标)
mylist=[1,2,3]
element=mylist.pop(2)
print(f"通过pop方法取出元素后列表内容：{mylist}，取出的元素是：{element}")

#7. 删除某元素在列表中的第一个匹配项
mylist=[1,2,3,2,3]
mylist.remove(2)  #remove删掉的是列表里的是这个内容的元素而不是下标的那个元素，而且只删第一个匹配的元素
print(f"通过remove方法移除元素后，列表结果是：{mylist}")

#8. 清空列表
mylist.clear()
print(f"列表被清空了，结果是:{mylist}")

#9. 统计列表内某元素的数量
mylist=[1,2,3,2,3]
count=mylist.count(2)
print(f"列表中2的数量是：{count}")

#10. 统计列表中全部的元素数量
mylist=[1,2,3,2,3]
count=len(mylist)
print(f"列表的元素数量总共有 {count} 个")