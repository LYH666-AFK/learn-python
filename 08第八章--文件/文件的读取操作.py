"""
演示对文件的读取
"""
#打开文件000
f=open("","r",encoding="UTF-8")
print(type(f))

#读取文件-read()
print(f"读取10个字节的结果：{f.read(10)}")
print(f"read方法读取全部内容的结果是：{f.read()}")    #连续调用read会接着上一次read之后开始

#读取文件-readLines()
lines=f.readlines()  #读取文件的全部行，封装到列表中
print(f"lines对象的类型{type(lines)}")
print(f"lines对象的内容是：{lines}")    #来自同一个文件对象，所以会接着上面内容，所以这样直接写会显示为空

#读取文件-readLine()
line1=f.readline()
line2=f.readline()
print(f"第一行数据是：{line1}")
print(f"第二行数据是：{line2}")

#for循环读取文件行
for line in f:
    print(f"每一行数据是：{line}")

#文件的关闭
f.close()

#with open 语法操作文件(自动关闭文件)
with open("","r",encoding="UTF-8")as f:    #执行完冒号后的内容就会关闭文件
    for line in f:
        print(f"每一行数据是：{line}")