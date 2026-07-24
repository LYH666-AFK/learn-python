"""
演示for循环的基础语法
"""

name="yufeng"
for x in name:
    print(x)

#案例
name="yufengshigaoshou"
count=0
for x in name:
    if x=="g":
        count+=1

print(f"被统计的字符串中有{count}个g")