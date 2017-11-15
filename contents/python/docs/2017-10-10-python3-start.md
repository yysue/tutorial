---
layout: post
title: "Python3入门笔记"
date: 2017-10-18 08:21:49
categories: Python
tags: Python
---


[Python3教程 - 廖雪峰](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)

# 环境

## 下载？

Python官网 https://www.python.org/downloads/

当前Python最新版本：

https://www.python.org/ftp/python/3.6.3/python-3.6.3.exe

https://www.python.org/ftp/python/2.7.14/python-2.7.14.msi


# Python基础

## 输入与输出

```shell
# 输出
print('hello, world')
print('100 + 200 =', 100 + 200)

# 输入
name = input('input your name:')

# 字符串连接
print(name, 'hello world')

# 保存成文件hello.py执行起来
python hello.py
```

## 数据类型和变量

> 整数、浮点数、字符串、布尔值、空值
>
> 16进制整数用0x作前缀
>
> 浮点数的科学计数法 1.23x109就是`1.23e9`，或者`12.3e8`，0.000012可以写成`1.2e-5`
>
> 布尔值只有Ture、False两种值，and or not3个运算
>
> 空值是None
>
> 常量的定义用通常是全部大写，Python没有任何机制保证常量不会被改变

```python
# 转义字符
print('I\'m ok.\"\t\\n')

# r''表示''内部的字符串默认不转义(原样输出)
print(r'I\'m ok.\"\t\\\n')

# 多行字符串的输出用'''str'''
print('''hello
world\n123
''')

# 还可以这样用哦  r'''str'''
print(r'''hello
world\n123
''')

# 理解Python变量的含义
a = 'ABC' # 解释器创建了字符串'ABC'和变量a，并把a指向'ABC'
b = a # 解释器创建了变量b，并把b指向a指向的字符串'ABC'
a = 'XYZ' # 解释器创建了字符串'XYZ'，并把a的指向改为'XYZ'，但b并没有更改

# Python有两种除法
print(10 / 3) # what? 整数与整数得到浮点数
print(10 // 3) # 这个得到整数

```
常见转义字符

![](http://7xkmkl.com1.z0.glb.clouddn.com/yysue/images/python3-escape-characters.png) 

## 字符串和编码

理解字符编码

> 计算机只能处理数字，所以得先把文本转换为数字
>
> 8比特(bit) = 1字节(byte)
>
> 1字节表示最大整数255
>
> 2字节表示最大整数65535
>
> 4字节表示最大整数4294967295
>
> 美国ASCII编码是1字节
>
> 中国制定GB2312编码来处理中文
>
> 日本制定Shift_JIS编码来处理日文
>
> 韩国制定Euc-kr编码来处理韩文
>
> Unicode大一统，通常是2个字节
>
> UTF-8编码，可变长编码

![](http://7xkmkl.com1.z0.glb.clouddn.com/yysue/images/python3-04.png) 

现在计算机系统通用的字符编码工作方式

> 在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者传输的时候，就转换为UTF-8编码
>
> 用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，
>
> 编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件

![0](http://7xkmkl.com1.z0.glb.clouddn.com/yysue/images/python3-01.png) 

> 浏览网页的时候，服务器会把动态生成的Unicode内容转换为UTF-8再传输到浏览器

![1](http://7xkmkl.com1.z0.glb.clouddn.com/yysue/images/python3-02.png) 

单个字符与整数编码的转化

```Python
# 单个字符转换成编码
print(ord('A'))
print(ord('中'))

# 编码转换成字符
print(chr(66))
print(chr(20013))
print(chr(0x4e2d))

# 16进制整数编码 Unicode字符串
print('\u4e2d\u6587') 
```

注意区分

```Python
# 是str(字符串)
print('ABC')

# 是bytes,每个字符只占用一个字节
print(b'ABC')
```

以Unicode表示的str通过encode()方法可以编码为指定的bytes

```Python
# 纯英文的字符串可用用ascii编码为bytes
print('ABC'.encode('ascii'))

# 含有中文的字符串可以用utf-8编码为bytes，在bytes中，无法显示为ASCII字符的字节，用\x##显示
print('中文'.encode('utf-8'))
```
如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。

要把bytes变为str，就需要用decode()方法

```Python
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
```

计算str包含多少个字符len()

```Python
# 计算str的字符数
len('ABC')
len('中文')
# 计算bytes的字节数
len(b'ABC')
len('中文'.encode('utf-8'))
len(b'\xe4\xb8\xad\xe6\x96\x87')
# 1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节
```

当Python源码中包含中文时，要保存为UTF-8编码

```Python
# 当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行
#!/usr/bin/env python3
# -*- codeing: utf-8 -*-
# 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释
# 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码
# 申明了UTF-8编码并不意味着你的.py文件就是UTF-8编码的，必须并且要确保文本编辑器正在使用UTF-8 without BOM编码
```

格式化，参考下图

![format](http://7xkmkl.com1.z0.glb.clouddn.com/yysue/images/01_3.png)
常见占位符(%s永远起作用)

| 点位符  | 含义                |
| ---- | ----------------- |
| %d   | 整数                |
| %f   | 浮点数,保留小数后一位用 %.1f |
| %s   | 字符串               |
| %x   | 十六进制整数            |
| %%   | 输出%               |

## 使用list和tuple
定义一个list

```Python
# list是一种有序集合
classmates = ['Michael', 'Bob', 'Tracy']
```

访问list

```Python
len(classsmates) # 获取list元素个数
classmates[0] # 从0开始,-1表示倒数第1个
```

对list中的元素进行操作

```Python
classmates.append('Adam') # 追加元素到末尾
classmates.insert(1, 'Jack') # 把元素插入到指定位置
classmates.pop() # 删除末尾元素
classmates.pop(1) # 删除指定位置元素
classmates[1] = True # 替换
# 注意:list里面的元素的数据类型可以不同
```

定义tuple

```Python
# tuple也是一种有序列表,叫元组,与list不同这处是初始化之后,不能修改
t = (1, 2, 3, 4)
t = (1, ) # 注意在定义只有一个元素的tuple时,加个逗号,以区分不是小括号,消除歧义
```

## 条件判断
```Python
if a:
	do something of a
elif b:
	do something of b
else:
	do something else
```

数据类型的转换

```Python
# input() 返回的数据类型是str
# str转换成int
age = int(s)
```

## 循环

for  in循环

```Python
names = ['Michael', 'Bob', 'Tracy']
for name in names:
	print(name)
# 计算1-100整数和
sum = 0
for x in range(101):
    sum += x
print(sum)
```

while循环

```Python
# 计算100之内所有奇数之和
sum = 0
n = 99
while n > 0:
	sum += n;
	n -= 2
print(sum)
```

break与continue

> break在循环过程中直接退出循环
> continue提前结束本轮循环，并直接开始下一轮循环

## 使用dict和set

定义dict

```Python
# dict是一组key-value集合
d = {'Michael':95, 'Bob':75, 'Tracy':85}
```

访问dict

```Python
d # 输出全部key-value
d['Michael'] # 不存在报错
'aaa' in d # 判断key是否存在
d.get('Michael') # 不存在返回None
d.get('aaa', -1) # 不存在就返回-1
```

操作dict

```Python
d['Jack'] = 90 # 插入一个key-value，如果key重复，后面的值冲掉前的值
d.pop('Bob') # 删除不存在的key会报错
```

list与dict比较

> dict:查找和插入不随key的增加而变慢，占用大量内存
> list:查找和插入随元素的增加而变慢，占用空间小
> dict的key是否不可变对象

定义set

```Python
# set是一组key集合，重复的key会被过滤
s = set([1, 2, 3, 3])
s # 打印set
```

操作set

```Python
s.add(4) # 添加重复key无效果
s.remove(4) # 删除不存在的key会报错
```

set可以进行集合操作

```Python
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s1 & s2
s1 | s2
```

set与dict区别

> 原理相同，set的key同样是不可变对象
> set没有存储对应的value

不可变对象

```Python
# str是不变对象，list是可变对象
l = ['c', 'b', 'a']
l.sort()
l # 此时l的顺序变了
s = 'abc'
s.replace('a', 'A')
s # 此时s并没有变
```

# 函数

## 调用Python内置函数

> [内置函数官方文档](https://docs.python.org/3/library/functions.html)

```Python
# abs()函数
abs(100)
abs(-20)
abs(12.34)
abs(1, 2) # 参数数量不对,报错TypeError
abs('a') # 参数类型不对,报错TypeError
# 数据类型转换函数
int('123')
int(12.34)
float('12.34')
str(12.34)
str(100)
bool(1) # True
bool('') # False
# 函数名是指向函数对象的引用,可以把函数名赋给一个变量,相当于给函数起别名
a = abs
a(-1)
```

## Python内置函数

> 根据3.5.2官方文档

```Python
abs() # 取绝对值
all() # 检查是否所有元素都可迭代
any() # 检查是否有元素可迭代
ascii() # 返回一个对象的可打印的表示
bin() # 将int类型转换成二进制字符串
bool() # 检查一个表达式是True,False
bytearray() # 返回一个字节数组
bytes() # 返回一个字节数组
callable() # 检查某个对象是否可调用(是否是函数)
chr() # 将整数转换成ascii
classmethod() # 返回一个函数的类方法
compile()
complex()
delattr()
dict()
dir()
divmod()
enumerate() # 可将list转换成索引-元素对
eval() # 执行一个字符串表达式
exec()
filter() # 过滤序列
float()
format()
frozenset()
getattr()
globals()
hasattr()
hash()
help()
hex()
id()
input()
int()
isinstance() # 检查某对象是否是某类的实例
issubclass()
iter() # 把list,dict,str等Iterable变成Iterator
len()
list()
locals()
map() # map将传入的函数依次作用到序列的每个元素,并把结果作为新的Iterator返回
max()
memoryview()
min()
next() # 获取生成器的下一个元素,没有抛出StopIteration错误
object()
oct()
open()
ord()
pow() # pow(x, y[, z]) x^y%z
print()
property()
range() # 返回一个序列list
repr()
reversed()
round()
set()
setattr()
slice()
sorted() # 对list进行排序
staticmethod()
str()
sum()
super()
tuple()
type()
vars()
zip()
__import__()
```

## 字符串方法

```Python
s.strip() # 判断是否为空
```

## 定义函数

定义一个函数

```Python
def my_abs(x):
	if x >= 0:
		return x
	else:
		return -x
# 如果没有return语句,返回None
# return None可以写成return
```

> 交互环境会有...提示符(定义函数时用),两次回车,回到>>>提示符下
> 把这段代码保存到文件abstest.py
> `from abstest import my_abs` 这句话导入该函数

空函数

```Python
def nop():
	pass
# pass语句什么都不做,作为占位符
```

定义函数要对参数做检查

```Python
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x
```

返回多个值

```Python
import math
def move(x, y, step, angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
# 返回多个值,其实是返回的一个值tuple或list
```

## 函数的参数

位置参数

```Python
# 计算x的平方
def power(x):
    return x * x
power(5)
power(15)
# 计算x的n次方
def power(x, n):
    s = 1
    while n > 0:
        n -= 1
        s *= x
	return s
power(5, 2)
power(5, 3)
```

默认参数

```Python
# 使用默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n -= 1
        s *= x
	return s
power(5)
power(5, 2) # 二者等价
```

> 使用默认参数,需要注意:
>
> 1. 必选参数在前,默认参数在后
> 2. 当函数有多个参数时,把变化大的参数放前面,变化小的参数放后面
>    比如:姓名,性别,年龄,城市

如果有多个默认参数,且默认参数不按顺序调用怎么办

```Python
# 小学生注册函数 v1
def enroll(name, gender):
    print('name:', name)
    print('gender:', gender)
# 小学生注册函数 v2
def enroll(name, gender, age=6, city='Beijing'):
	print('name:', name)
	print('gender:', gender)
	print('age:', age)
	print('city:', city)
# 所有6岁的北京小孩可以如下调用了
enroll('Adam', 'M')
# 如果是6岁的南京小孩怎样调用最简单呢
enroll('Jam', 'F', city='Nanjing')
```

默认参数的一个坑

```Python
def add_end(L=[]):
	L.append('END')
	return L
# 这样调用是正常的
add_end([1, 2, 3])
add_end(['x', 'y', 'z'])
# 使用默认参数,第一次调用也是正常的,再次调用就不正常了
>>> add_end()
['END']
>>> add_end()
['END', 'END']
>>> add_end()
['END', 'END', 'END']
```

> 解释:Python函数在定义的时候,默认参数L的值就被计算出来了,即[],
> 因为默认参数L也是一个变量,它指向对象[],每次调用该函数,
> 如果改变了L的内容,则下次调用时,默认参数的内容就变了,不再是函数定义时的[]了
> 避免这个坑:默认参数必须指向不变对象

修正这个坑

```Python
def add_end(L=None):
	if L is None:
		L = []
	L.append('END')
	return L
```

> 为什么要设计str,None这样的不变对象呢?因为不变对象一旦创建,对象内部的数据就不能修改,这样就减少了由于
> 修改数据导致的错误.此外,由于对象不变,多任务环境一同时读取对象不需要加锁,同时读取一点问题都没有
> 我们在编写程序时,如果可以设计一个不变对象,那就尽量设计成不变对象

可变参数

```Python
# 参数个数不确定,用list
def calc(numbers):
    sum = 0
    for n in numbers:
        sum += n * n
	return sum
# 调用时,需要先组装一个list或tuple
calc([1, 2, 3])
# 把参数改成可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n * n
	return sum
calc(1, 2, 3)
# 问题,已经存在的一个list或tuple作为参数调用这个函数咋办
nums = [1, 2, 3]
calc(*nums)
# *nums表示把nums这个list的所有元素作为可变参数传进去
```

关键字参数

```Python
def person(name, age, **kw):
	print('name:', name, 'age:', age, 'other:', kw)
# 可变参数允许传入0个或任意个参数,在函数调用时自动组装为一个tuple
# 关键字参数允许传入0个或任意个含参数名的参数,在函数调用时自动组装为一个dict
# 关键字参数是可选的
>>> person('Michael', 30)
name: Michael age: 30 other: {}
>>> person('Michael', 30, city='Beijing')
name: Michael age: 30 other: {'city': 'Beijing'}
>>> person('Michael', 30, city='Beijing', job='Engineer')
name: Michael age: 30 other: {'city': 'Beijing', 'job': 'Engineer'}
>>> person('Michael', 30, city='Beijing', job='Engineer', gender='M')
name: Michael age: 30 other: {'city': 'Beijing', 'job': 'Engineer', 'gender': 'M'}

# 如果一个已经定义了的dict,想作为关键字参数调用这个函数
extra = {'city': 'Beijing', 'job': 'Engineer', 'gender': 'M'}
person('Jack', 24, **extra)
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数
# kw将获得一个dict,注意kw获得的dict是extra的一份拷贝,对kw的改动不会影响到函数外的extra
```

命名关键字参数

```Python
# 定义一个有命名关键字参数的函数
def person(name, age, *, city, job):
	print(name, age, city, job)
# 如果函数定义中已经有一个可变参数,后面跟着的命名关键字参数就不再需要一个特殊分隔符(*)了
def person(name, age, *args, city, job):
	print(name, age, args, city, job)
# 命名关键字参数如果声明了,在调用函数时,就一定要传入
# 对于命名关键字参数,可以设置默认参数
```

参数组合

> 在Python中定义函数,有必选参数,默认参数,可变参数,命名关键字参数,关键字参数
> 这5种参数可组合使用,参数定义的顺序必须是:
> 必选参数,默认参数,可变参数,命名关键字参数,关键字参数

```Python
def f1(a, b, c=0, *args, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'args=', args, 'kw=', kw)
def f2(a, b, c=0, *, d, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'd=', d, 'kw=', kw)
# 对于任意函数,都可以通过类似func(*args, **kw)的形式调用它,无论它的参数是如何定义的
```

## 递归函数

斐波那契数列

```Python
def fact(n):
	if n==1:
		return 1
    return n * fact(n-1)
# 效率不高,栈溢出
# 尾递归优化
def fact(n):
	return fact_iter(n, 1)
def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
```

汉诺塔

```Python
# 请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法
# move(3, 'A', 'B', 'C') 期待输出:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
	else:
        move(n-1, a, c, b)
        print(a, '-->', c)
        move(n-1, b, a, c)
```

# 高级特性

## 切片

取一个list或tuple的前n个元素

```Python
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
L[0:3] 
L[:3] # 取0,1,2这3个元素
L = list(range(100))
L[:10] # 取前10个数
L[-10:] # 取后10个数
L[10:20] # 取11到20个数
L[:10:2] # 取前10个数,每2个取1个
L[::5] # 所有数,每5个取1个
L[:] # 原样复制一个list
# tuple和字符串都可以看成是一个list,只是不可变
```

## 迭代

```Python
# 几种迭代形式
for key in d:
    pass
for k, v in d.items():
    pass
for ch in 'ABC':
    pass
for i, v in enumerate(['A', 'B', 'C']):
    pass
for x, y in [(1, 1), (2, 4), (3, 9)]:
    pass
# 判断某对象是否可迭代
from collections import Iterable
isinstance('abc', Iterable)
```

## 列表生成式

```Python
# 生成[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(range(1, 11))
# 生成[1*1, 2*2, 3*3, ..., 10*10]
# 繁
L = []
for x in range(1, 11):
    L.append(x * x)
# 简
[x * x for x in range(1, 11)]
# 还可以加筛选,公偶数的平方
[x * x for x in range(1, 11) if x % 2 == 0]
# 使用两层循环,生成全排列
[m + n for m in 'ABC' for n in 'XYZ']
# 列出当前目录下的所有文件名与目录名
import os
[d for d in os.listdir('.')]
# 把dict转换成list
d = {'x':'A', 'y':'B', 'z':'C'}
[k + '=' + v for k, v in d.items()]
# 把list中所有字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
[s.lower() for s in L]
```

## 生成器

> 通过列表生成式,可以直接创建一个列表
> 如果列表元素可以按照某种算法推算出来,
> 那我们是否可以在循环过程中推算出后续元素,
> 这样就不必创建完整的list,从而节省大量的空间
> 在Python中,这种一边循环一边计算的机制,称为生成器:generator

定义一个生成器

```Python
# 定义一个列表
L = [x * x for x in range(10)]
# 定义一个生成器
g = (x * x for x in range(10))
# 比较其不同
>>> L
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> g
<generator object <genexpr> at 0x1097e7938>
```

使用生成器

```Python
next(g) # 获取生成器中下一个元素,一般不用
for n in g:
    print(n)
```

定义生成器的另一种方法

```Python
# 打印斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1 # 牛逼的赋值语句
    while n < max:
        print(b)
        a, b = b, a + b
	return 'done'
# fib函数实际上是定义了斐波拉契数列的推算规则,可以从第一个元素开始,推算出后续任意的元素,
# 这种逻辑其实非常类似generator
# 把fib函数变成generator,只需把print(b)改为yield b
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
	return 'done'
# 如果一个函数定义中包含yield关键字,这个函数不是普通函数,而是generator
>>> f = fib(6)
>>> f
<generator object fib at 0x10648f938>
# 理解函数与generator的执行流程不同
# 函数是顺序执行,遇到return或函数最后一句就返回
# 变成generator的函数,在每次调用next()时执行,
# 遇到yield语句返回,再次调用next()时从上次yield语句处执行
for n in fib(6):
    print(n)
# for循环拿不到返回值'done',需要捕获StopIteration错误
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
	except StopIteration as e:
        print('Generator return value:', e.value)
        break
```

杨辉三角

```Python
#          1
#        1   1
#      1   2   1
#    1   3   3   1
#  1   4   6   4   1
#1   5   10  10  5   1

# 定义
def triangles():
	L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i-1] + L[i] for i in range(len(L))]
# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
```

## 迭代器

> 可以直接作用于for循环的数据类型有:
> 一类是集合数据类型,如list,tuple,dict,set,str
> 一类是generator,包括生成器和带yield的generator function
> 这些可以直接作用于for循环的对象统称为可迭代对象Iterable
> 可以使用isinstance()判断一个对象是否是Iterable对象
> 可以被next()函数调用并不断返回下一个值的对象称为迭代器:Iterator
> 生成器都是Iterator对象,但list,dict,str虽然是Iterable,却不是Iterator
> 把list,dict,str等Iterable变成Iterator可用iter()函数

```Python
# 判断Iterable
from collections import Iterable
isinstance([], Iterable)
isinstance({}, Iterable)
isinstance('abc', Iterable)
isinstance((x for x in range(10)), Iterable)
isinstance(100, Iterable)
# 判断Iterator
from collections import Iterator
isinstance((x for x in range(0)), Iterator)
isinstance([], Iterator)
isinstance({}, Iterator)
isinstance('abc', Iterator)
# 将Iterable转化为Iterator
isinstance(iter([]), Iterator)
isinstance(iter({}), Iterator)
isinstance(iter('abc'), Iterator)
```

为啥list,dict,str等数据类型不是Iterator?

> 这是因为Python的Iterator对象表示的是一个数据流,Iterator对象可以被next()函数调用并不断返回下一个数据,
> 直到没有数据时抛出StopIteration错误.可以把这个数据流看做是一个有序序列,但我们却不能提前知道序列的长度,
> 只能不断通过next()函数实现按需计算下一个数据,所以Iterator的计算是惰性的,只有在需要返回下一个数据时它才会计算
> Iterator甚至可以表示一个无限大的数据流,例如全体自然数,而使用list是永远不可能存储全体自然数的

小结

> 凡是可作用于for循环的对象都是Iterable类型
> 凡是可作用于next()函数的对象都是Iterator类型,它们表示一个惰性计算的序列
> Python的for循环本质上就是通过不断调用next()函数实现的

```Python
for x in [1, 2, 3, 4, 5]:
	pass
# 与下面这段等价
it = iter([1, 2, 3, 4, 5])
while True:
    try:
        x = next(it)
	except StopIteration:
        break
```

# 函数式编程

> 函数式编程的一个特点就是,允许把函数本身作为参数传入另一个函数,还允许返回一个函数
> Python对函数式编程提供部分支持,由于Python允许使用变量,因此,Python不是纯函数式编程语言

## 高阶函数

> 编写高阶函数,就是让函数的参数能够接收别的函数
> 把函数作为参数传入,这样的函数称为高阶函数
> 函数式编程就是指这种高度抽象的编程范式

变量可以指向函数

```python
abs(-10) # 这是函数调用
abs # 这是函数本身
x = abs(-10) # 把函数调用结果赋值给变量
f = abs # 把函数本向赋值给变量,变量可以指向函数
f(-10) # 通过变量调用函数
```

函数名也是变量

```Python
abs = 10 # 也可以指向其他对象,要恢复就得重启Python交互环境
```

传入函数

```Python
def add(x, y, f):
    return f(x) + f(y)
add(-4, 4, abs)
```

### map/reduce

> Google论文[MapReduce](https://research.google.com/archive/mapreduce.html)

map函数

```Python
# map函数接收两个参数,一个是函数,一个是Iterable
# map将传入的函数依次作用到序列的每个元素,并把结果作为新的Iterator返回
# 计算y=x^2
def f(x):
    return x*x
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
list(r)
# 将list中的数字转化为字符串
```

reduce函数

```Python
# reduce把一个函数作用在一个序列上,这个函数必须接收两个参数,reduce把结果继续和序列的下一个元素做累积计算
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# 对一个序列求和
from functools import reduce
def add(x, y):
    return x + y
reduce(add, [1, 3, 5, 7, 9])
# str转int
def fn(x, y):
    return x * 10 + y
def char2num(s):
    return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]
reduce(fn, map(char2num, '1221'))
# 用lambda函数简化
def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
```

几个练习

```Python
# 练习一
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
# -*- coding: utf-8 -*-
def normalize(name):
    return name.capitalize()
# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
# --------------------------------------------------------------
# 练习二
# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积
from functools import reduce
def prod(L):
    return reduce(lambda x, y: x*y, L)
# 测试
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# --------------------------------------------------------------
# 练习三
# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
def str2float(s):
    f1 = lambda x: {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[x]
    L = s.split('.')
    a = reduce(lambda x, y: x * 10 + y, map(f1, L[0]))
    if len(L) == 2:
        b = reduce(lambda x, y: x * 0.1 + y, map(f1, L[1][::-1]))
    return a + b * 0.1
# 测试
print('str2float(\'123.456\') =', str2float('123.456'))
```

一个字符串倒序

```Python
s = '123'
# 转换成list,调用list的reverse()函数
L = list(s)
L.reverse()
# 用切片
s[::-1]
```



### filter

> 接收一个函数和一个序列,把传入的函数依次作用于每个元素,然后根据返回值是True或False决定保留还是丢弃该元素

```Python
# 一个list中删掉偶数,保留奇数
list(filter(lambda x: x%2==1, [1, 2, 4, 5, 6, 9, 10, 15]))
# 一个序列中的空字符串删掉
list(filter(lambda x: x and x.strip(), ['A', '', 'B', None, 'C', '  ']))
# filter()函数返回的是一个Iterator,也就是一个惰性序列,所以要强迫filter()完成计算结果
# 需要用list()函数获得所有结果并返回list
```

用filter求素数

> 质数（prime number）又称素数，有无限个。质数定义为在大于1的自然数中，除了1和它本身以外不再有其他因数的数称为质数。
> 方法[埃拉托色尼筛选法](http://baike.baidu.com/view/3784258.htm)

```Python
# 先构造一个从3开始的奇数序列,这是一个生成器,并且是一个无限序列
def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n
# 定义一个筛选函数, 返回一个匿名函数
def _not_divisible(n):
    return lambda x: x % n > 0
# 定义一个生成器,不断返回下一个素数
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列
# 这个生成器先返回第一个素数2,然后利用filter不断产生筛选后的新序列
# 打印1000以内的素数
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
```

用filter过滤掉回数

```Python
# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数：
def is_palindrome(n):
    s = str(n)
    return s == s[::-1]
# 测试:
output = filter(is_palindrome, range(1, 1000))
print(list(output))
# 牛逼 s[::-1]可以实现字符串的倒序
```

### sorted

> 对list进行排序

```Python
sorted([36, 5, -12, 9, -21])
# 自定义排序
sorted([36, 5, -12, 9, -21], key=abs)
# key指定的函数将作用于list的每个元素上,并根据key函数返回的结果进行排序
# 按字母排序,忽略大小写
sorted(['Bob', 'about', 'Zoo', 'Credit'], key=str.lower)
# 反向排序
sorted(['Bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
```

## 返回函数

函数作为返回值

```Python
# 实现一个可变参数求和
def calc_sum(*args):
    ax = 0
    for n in args:
        ax += n
    return ax
# 如果不需要立刻求和,而是在后面的代码中,根据需要再计算求和
# 可以不返回求和的结果而返回求和的函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
		return ax
    return sum
f = lazy_sum(1, 3, 5, 7, 9)
f # f是一个函数
f() # 调用这个函数
```

> 在这个例子中,我们在函数lazy_sum中又定义了函数sum,并且,内部函数sum可以引用外部
> 函数lazy_sum的参数和局部变量,当lazy_sum返回函数sum时,相关参数和变量都保存在返回的
> 函数中,这种称为"闭包(Closure)"的程序结构拥有极大的威力
> 再注意一点,当我们调用lazy_sum()时,每次调用都会返回一个新的函数,
> 即使传入相同的参数
>
> ```Python
> f1 = lazy_sum(1, 3, 5, 7, 9)
> f2 = lazy_sum(1, 3, 5, 7, 9)
> f1 == f2 # 返回False
> ```
>
> f1()和f2()的调用结果互不影响

闭包

> 注意:
> 1.返回的函数在其定义内部引用了局部变量args,所以,当一个函数返回了一个函数后,其内部的
> 局部变量还普查新函数引用
> 2.返回的函数并没有立刻执行,而是直到调用了f()才执行

```Python
def count():
	fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
	return fs
f1, f2, f3 = count()
# 调用这3个函数
f1() # 返回9
f2() # 返回9
f3() # 返回9
# 全部都是9,原因在于返回的函数引用了变量i,但它并非立刻执行,等到3个函数都返回时,它所引用的变量i已经变成了3,
# 因此最终结果为9
# 个人小实验
def test():
    fs = []
    i = 3
    def f():
        print(i)
        return i
    fs.append(f)
    i = 4
    def g():
        print(i)
        return i
    fs.append(g)
    return fs
f, g = test()

# 返回闭包时牢记的一点就是:返回函数不要引用任何循环变量,或者后续会发生变化的变量
# 一定要引用循环变量怎么办?方法是再创建一个函数,用该函数的参数绑定循环变量当前的值,
# 无论该循环变量后续如何更改,已绑定到函数参数的值不变
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)被立刻执行,因此i的当前值被传入f()
	return fs
f1, f2, f3 = count()
f1() # 返回1
f2() # 返回4
f3() # 返回9
```

小结

> 一个函数可以返回一个计算结果,也可以返回一个函数
> 返回一个函数时,牢记该函数并未执行,返回函数中不要引用可能会变化的变量

## 匿名函数

```Python
list(map(lambda x: x*x, [1, 2 ,3 ,4, 5, 6, 7, 8, 9]))
# lambda x: x*x实际上是
def f(x):
    return x*x
# 关键字lambda表示匿名函数,冒号前而的x表示函数参数
# 匿名函数有个限制,就是只有一个表达式,不用写return,返回值就是该表达式的结果
# 匿名函数不必担心函数名冲突,
# 匿名函数也是一个函数对象,也可以把匿名函数赋值给一个变量
# 再利用变量来调用该函数
# 也可以把匿名函数作为返回值返回
```

## 装饰器

函数对象有一个`__name__`属性,可以拿到函数的名字

```Python
def now():
    print('2015-3-25')
f = now
f()
now.__name__
f.__name__
abs.__name__
```

> 现在,假设我们要增加now()函数的功能,比如,在函数调用前后自动打印日志,但又不希望修改now()函数的定义
> 这种在代码在运行期间动态增加功能的方式,称这为"装饰器"(Decorator)

```Python
import functools
# 本质上,decorator就是一个返回函数的高阶函数,所以,我们要定义一个能打印日志的decorator
def log(func):
    @functools.wraps(func)  # 不加这个,now.__name__会输出wrapper的
    def wrapper(*args, **kw):
        print('cal %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
# 借助@讲法,把decorator置于函数的定义处
# 相当于执行了now = log(now)
@log
def now():
    print('2015-3-25')
# 如果decorator本身需要传入参数,那就需要编写一个返回decorator的高阶函数,比如自定义log的文本
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
# 这个3层嵌套的decorator用法如下
@log('execute')
def now():
    print('2015-3-25')
# 与2层嵌套的decorator相比,3层嵌套的效果是这样的
now = log('execute')(now)

# 还差一步,现在如果执行
now.__name__ # 应该输出now而不是wrapper
#在wrapper()的前面加上@functools.wraps(func)即可
```

写一个@log的decorator支持log()和log('execute')

```Python
def log(*pargs):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('begin call')
            text = 'hello'
            if len(pargs) > 0:
                text = pargs[0]
            print('%s %s():' % (text, func.__name__))
            ret = func(*args, **kw)
        	print('end call')
            return ret
        return wrapper
    return decorator

@log('execute', 'ffff')
def now():
    print('2015-3-25')
```

## 偏函数

> 偏函数(Partial function)的作用就是,把一个函数的某些参数固定住(也就是设置默认值),
> 返回一个新的函数

```Python
# 默认转换为10进制
int('12345')
# 转换为8进制
int('12345', base=8)
def int8(x, base=8):
    return int(x, base)
# 用偏函数定义
import functools
int8 = functools.partial(int, base=8)
```

# 模块

> 一个.py文件就称为一个模块
> 好处是提高了代码的可维护性,避免名字冲突
> 分为Python内置模块和第三方模块
> 一个abc.py的文件就是一个名字叫做abc的模块
> 模块上还有包,包就是包含abc.py的目录名(假设是mycompany),避免模块名冲突
> 每个包目录下会有一个`__init__.py`文件
> 这个文件是必须存在的,否则,Python就把这个目录当成普通目录,而不是一个包
> `__init__.py`可以是空文件,也可以有Python代码,因为它本身就是一个模块
> ,而它的模块名就是包名mycompany
> 可以有我级目录,组成多级层次的包结构
>
> ```Python
> mycompany
> 	web
> 		__init__.py
> 		utils.py
> 		www.py
> 	__init__.py
> 	abc.py
> 	utils.py
> 	xyz.py
> # www.py的模块名就是mycompany.web.www
> # 两个utils.py的模块名分别是mycompany.web.utils和mycompany.utils
> # 创建模块时要注意命名,不能和Python自带的模块名称冲突
> # 如系统自带了sys模块,自己的模块就不可命名为sys.py,否则将无法导入系统自带的sys模块
> # ?不同的包下也不行吗????
> ```
>
> 

## 使用模块

编写一个hello模块hello.py

```Python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module'

__author__ = 'ln_ydc'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__ == '__main__':
    test()
```

> 第1行和第2行是标准注释,第1行注释可以上这个hello.py文件直接运行在Unix/Linux/Mac上运行
> 第2行注释表示.py文件本身使用标准UTF-8编码
> 第4行是一个字符串,表示模块的文档注释,任何模块代码的第一个字符串都被视为模块的文档注释
> 第6行使用`__author__`变量把作者写进去

调用模块

> 导入sys模块后,我们就有了变量sys指向该模块,利用该模块,可以访问sys模块的所有功能
> sys模块有一个argv变量,用list存储了命令行的所有参数,argv至少有一个元素,因为第一个参数永远是该.py文件的名称
> python3 hello.py 获得的sys.argv就是['hello.py']
> 运行python3 hello.py Michael获得的sys.argv就是['hello.py', 'Michael']
> 我们在运行hello模块文件时,Python解释器把一个特殊变量`__name__`置为`__main__`,而如果在其他地方导入该模块时,
> if判断将失败,因此,这种if测试可以让一个模块通过命令行运行进执行一些额外的代码,
> 最常见的就是运行测试

```Python
# 命令行运行hello.py
python3 hello.py
python3 hello.py Michael
#如果启动Python交互环境,再导入hello模块
python3
improt hello
# 不会打印hello, world,因为没有执行test()函数
```

作用域

> 正常的函数变量名是公开的(public),可以被直接引用,比如 abc, x123, PI
> 类似`__xxx__`这样的变量是特殊变量,可以被直接引用,但是有特殊用途,比如上面的`__author__`, `__name__`就是特殊变量
> hello模块定义的文档注释也可以用特殊变量`__doc__`访问,我们自己的变量一般不要用这种变量名
> 类似`_xxx`和`__xxx`这样的函数或变量就是非公开的(private),不应该被直接引用,比如`_abc`, `__abc`
> private函数和变量"不应该"被直接引用,而不是"不能"被直接引用,是因为Python并没有一种方法可以完全限制访问
> private 函数或变量,但是,从编程习惯上不应该引用private函数或变量

```Python
def _private_1(name):
    return 'Hello, %s' % name
def _private_2(name):
    return 'Hi, %s' % name
def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
```

> 我们在模块里公开greeting()函数,而把内部逻辑用private函数隐藏起来,这样,调用greeting()函数不用关心内部的private函数细节,这也是一种非常有用的代码封装和抽象的方法:
> 外部不需要引用的函数全部定义成private,只有外部需要引用的函数才定义为public

## 安装第三方模块

> 确保安装pip
> mac或Linux上有可能并存Python3.x和Python 2.x,因此对应的pip命令是pip3

安装一个第三方库—Python Image Library

> 基于PIL的Pillow项目
> 一般,第三方库都会在Python官方的[pypi.python.org](https://pypi.python.org/)网站注册,
> 要安装一个第三方库,必须先知道该库的名称,可以在官网或者pypi上搜索

```Python
# 安装Pillow的命令
pip3 install Pillow
# 找个图片生成缩略图
from PIL import Image
im = Image.open('test.jpg')
print(im.format, im.size, im.mode)
# JPEG (343, 499) RGB
im.thumbnail((200, 100))
im.save('thumb.jpg', 'JPEG')
```
> 常用的第三文库还有

```Python
mysql-connector-python # MySQL的驱动
numpy #用于科学计算的NumPy库
Jinja2 # 用于生成文本的模板工具
```

模块的搜索路径

```Python
# 当我们试图加载一个模块时,Python会在指定的路径下搜索对应的.py文件,如果找不到,就会报错
import mymodule
# 默认情况下,Python解释器会搜索当前目录,所有已安装的内置模块和第三方模块,搜索路径存放在sys模块的path变量中
import sys
sys.path
```

如果要添加自己的搜索目录,有两种方法

```Python
# 一是直接修改sys.path,添加要搜索的目录
# 这种方法是在运行时修改,运行结束后失效
import sys
sys.path.append('/Users/hello/my_py_scripts')
# 第二种方法是设置环境变量PYTHONPATH,该变量的内容会被自动添加到模块搜索路径中,
# 注意只需要添加你自己的搜索路径,Python自己本身的搜索路径不受影响
```