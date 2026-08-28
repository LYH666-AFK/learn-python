"""
演示字典的常用操作
"""
my_dict={"jack":99,"lisa":88,"alan":77}
#新增元素
my_dict["amy"]=66
print(f"字典通过新增元素后，结果是：{my_dict}")

#更新元素
my_dict["jack"]=33
print(f"字典经过更新后，结果是：{my_dict}")

#删除元素
score=my_dict.pop("jack")
print(f"字典中移除了一个元素，结果是：{my_dict}，jack的考试分数是：{score}")

#清空元素
my_dict.clear()
print(f"字典被清空了，内容是：{my_dict}")

#获取全部的key
my_dict={"jack":99,"lisa":88,"alan":77}
keys=my_dict.keys()
print(f"字典的全部keys是：{keys}")

#遍历字典
#方法1：通过获取到全部的key来完成遍历
for key in keys:
    print(f"字典的key是：{key}")
    print(f"字典的value是：{my_dict[key]}")
#方法2：直接对字典进行for循环，每一次循环都是直接得到key
for key in my_dict:
    print(f"字典的key是：{key}")
    print(f"字典的value是：{my_dict[key]}")
#字典不支持下标索引，索引不能用while

#统计字典内的元素数量，len()函数
num=len(my_dict)
print(f"字典中的元素数量有：{num}个")