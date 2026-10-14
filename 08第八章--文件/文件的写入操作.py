"""
演示文件的写入
"""

#打开文件，不存在的文件，r,w,a
f=open("","w",encoding="UTF-8")      #文件不存在w会创建文件
#write写入
f.write("Hello World")      #文件是空的，因为这样写是写在内存里
# #flush刷新
f.flush()                   #将内存中积攒的内容，写入到硬盘的文件中
#close关闭
f.close()                   #close内置了flush的功能
#打开一个存在的文件
f=open("","w",encoding="UTF-8")
#write写入,flush刷新
f.write("")      #相当于重写内容，而非追加内容
#close关闭
f.close()