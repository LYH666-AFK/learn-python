"""
演示对list列表的循环，使用while和for循环2种方式
"""
def list_while_func():
    """
    使用while循环遍历列表的演示函数
    :return:None
    """
    mylist=[1,2,3]
    #定义一个变量标记列表下标
    index=0
    while index<len(mylist):
        element=mylist[index]
        print(f"列表的元素：{element}")
        index+=1


def list_for_func():
    """
    使用for循环遍历列表的演示函数
    :return:
    """
    mylist=[1,2,3]
    for element in mylist:
        print(f"列表的元素有：{element}")


list_while_func()
list_for_func()