#代码开头
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
' a test module '
__author__ = 'Michael Liao

#添加搜索目录
import sys
sys.path.append('/Users/michael/my_py_scripts')
#r'防转置
Image.open(r'D:\path\to\test.jpg')








#汉罗塔
def move(n,a,b,c):
    if n>1:
        move(n-1,a,c,b)
        print('%s -->%s'%(a,c))
        move(n-1,b,a,c)
    else:
        print('%s -->%s'%(a,c))

move(3,'a','b','c')
#菲波那切数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
#如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


#杨辉三角迭代器
def triangles():
    N = [1]
    while True:
        yield N
        N.append(0)
        N = [N[i-1] + N[i] for i in range(len(N))]


'''最开始是 N【1】 然后 N.append(0) 就变成了 【1，0】 那个循环长度为2
那么第一次 新N【0】=N【-1】+N【0】=1（N【-1】就是倒数最后一个元素） 第二次 新N【1】=N【0】+ N【1】=1 所以此时的N 就是 【1，1】
以此类推 第二排 N=【1，1，0】（循环次数等于长度）
第一次循环 新N【0】=N【-1】+N【0】=1 新N【1】=N【0】+N【1】=2 新 N【2】=N【1】+N【2】=1 '''


n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break

#输出全体整数
def iterator():
    i=1
    while True:
        yield i
        i += 1
o = iterator()

while True:
    try:
        x = next(o)
        print(x)
    except StopIteration:
        break

#mapmap()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
list(r)
[1, 4, 9, 16, 25, 36, 49, 64, 81]

#reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce
def add(x, y):
    return  x + y

reduce(add, [1, 3, 5, 7, 9])
25

#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2floatGt0(s):
    return reduce(lambda x,y: x*10 + y, map(char2num,s))

def str2floatLt0(s):
    return (reduce(lambda x,y: 0.1*x + y, map(char2num, s[::-1]))/10)

def str2float(s):
    pointIndex = s.index('.')
    return str2floatGt0(s[:pointIndex]) + str2floatLt0(s[(pointIndex+1):])


#和map()类似，filter()也接收一个函数和一个序列。和map()不同的时，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
#注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。
#filter()的作用是从一个序列中筛出符合条件的元素。由于filter()使用了惰性计算，所以只有在取filter()结果的时候，才会真正筛选并每次返回下一个筛出的元素。


'''请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。

再思考一下能否写出一个@log的decorator，使它既支持：

@log
def f():
    pass
又支持：

@log('execute')
def f():
    pass'''


import functools
def log(text):
    if isinstance(text, (str, int, float)):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('start %s %s():' % (text, func.__name__))
                result = func(*args, **kw)
                print('end %s %s():' % (text, func.__name__))
                return result
            return wrapper
        return decorator
    else:
        func = text
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('start call %s():' % func.__name__)
            result = func(*args, **kw)
            print('end call %s():' % func.__name__)
            return result
        return wrapper



@log
def f():
    print('good')


@log('bad')
def f():
    print('good')

f()

#面向对象
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))


#仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
 class MyObject(object):
     def __init__(self):
         self.x = 9
     def power(self):
        return self.x * self.x

obj = MyObject()
#紧接着，可以测试该对象的属性：

hasattr(obj, 'x') # 有属性'x'吗？
True
obj.x
9
hasattr(obj, 'y') # 有属性'y'吗？
False
setattr(obj, 'y', 19) # 设置一个属性'y'
hasattr(obj, 'y') # 有属性'y'吗？
True
getattr(obj, 'y') # 获取属性'y'
19
obj.y # 获取属性'y'
19
#可以传入一个default参数，如果属性不存在，就返回默认值：

getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
404

#还可以尝试给实例绑定一个方法：
s = Student()
def set_age(self, age): # 定义一个函数作为实例方法
     self.age = age

from types import MethodType
 s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
 s.set_age(25) # 调用实例方法
 s.age # 测试结果
25

#为了给所有实例都绑定方法，可以给class绑定方法：

def set_score(self, score):
     self.score = score

Student.set_score = MethodType(set_score, Student)


