#用while遍历list
first_list=[1,2,3,4,5,6,7,8,9,10]
second_list=[]
index=0
while index<len(first_list):
    if first_list[index]%2==0:
        second_list.append(first_list[index])
    index+=1
print(f"通过while循环，从列表{first_list}中取出偶数，组成新列表：{second_list}")


#用for循环遍历list
first_list=[1,2,3,4,5,6,7,8,9,10]
second_list=[]
for i in first_list:
    if i%2==0:
        second_list.append(i)
print(f"通过for循环，从列表{first_list}中取出偶数，组成新列表：{second_list}")