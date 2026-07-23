"""
用while输出九九乘法表
"""
i=1
while i<=9:

    j=1
    while j<=i:
        print(f"%d*%d=%d\t" % (j, i, j * i),end='')
        j+=1

    i+=1
    print()

#print()就是输出换行，即让外层循环换行而此程序内循环依旧按照end=''不换行，就实现了九九乘法表的形式，\t是对齐