"""
演示字典的课后练习
"""
my_dict={
    "小明":{"部门":"科技部","工资":3000,"级别":1},"小红":{"部门":"市场部","工资":5000,"级别":2},
    "小华":{"部门":"市场部","工资":7000,"级别":3},"小刚":{"部门":"科技部","工资":4000,"级别":1},
    "小方":{"部门":"6000","工资":1,"级别":2}
}
print(my_dict)
for name in my_dict:
    if my_dict[name]["级别"]==1:
        employee=my_dict[name]
        employee["级别"]=2
        employee["工资"]+=1000
        my_dict[name]=employee
print(my_dict)