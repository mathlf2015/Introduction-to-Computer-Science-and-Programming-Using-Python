def fun1(n):
    if n==1 or n==2:
        return 1
    else:
        return fun1(n-1)+fun1(n-2)
    
number = int(input("输入一个数字:"))
result=fun1(number)
print("%d的斐波那契数列结果是:%d"%(number,result))

    
