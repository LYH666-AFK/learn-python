"""
演示数据容器通用功能
"""
my_list=[1,2,3,4,5]
my_tuple=(1,2,3,4,5)
my_str="abcdefg"
my_set={1,2,3,4,5}
my_dict={"key1":1,"key2":2,"key3":3,"key4":4,"key5":5}

#len元素个数
print(f"列表元素个数有：{len(my_list)}")
print(f"元组元素个数有：{len(my_tuple)}")
print(f"字符串元素个数有：{len(my_str)}")
print(f"集合元素个数有：{len(my_set)}")
print(f"字典元素个数有:{len(my_dict)}")

#max最大元素
print(f"列表最大的元素是：{max(my_list)}")
print(f"元组最大的元素是：{max(my_tuple)}")
print(f"字符串最大的元素是：{max(my_str)}")
print(f"集合最大的元素是：{max(my_set)}")
print(f"字典最大的元素是:{max(my_dict)}")

#min最小元素
print(f"列表最小的元素是：{min(my_list)}")
print(f"元组最小的元素是：{min(my_tuple)}")
print(f"字符串最小的元素是{min(my_str)}")
print(f"集合最小的元素是：{min(my_set)}")
print(f"字典最小的元素是：{min(my_dict)}")

#想要各个容转换，只要用想转换的容器名加在前面就行   如list(my_set),set(my_list)

#进行容器排序
print(f"列表对象的排序结果：{sorted(my_list)}")
print(f"元组对象的排序结果：{sorted(my_tuple)}")
print(f"字符串对象的排序结果：{sorted(my_str)}")
print(f"集合对象的排序结果：{sorted(my_set)}")
print(f"字典对象的排序结果:{sorted(my_dict)}")

print(f"列表对象的反向排序结果：{sorted(my_list,reverse=True)}")
print(f"元组对象的反向排序结果：{sorted(my_tuple,reverse=True)}")
print(f"字符串对象的反向排序结果：{sorted(my_str,reverse=True)}")
print(f"集合对象的反向排序结果：{sorted(my_set,reverse=True)}")
print(f"字典对象的反向排序结果:{sorted(my_dict,reverse=True)}")