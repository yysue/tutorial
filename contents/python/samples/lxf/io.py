# -*- coding: utf-8 -*-
import os

print os.name
# print os.uname()
# 查看当前目录的绝对路径
print os.path.abspath('.')
# 路径合并
testdir = os.path.join(os.path.abspath('.'), 'testdir')
print testdir
# 创建目录
os.mkdir(testdir)
# 删除目录
os.rmdir(testdir)
# 路径拆分
print os.path.split(testdir)
# 得到文件扩展名
print os.path.splitext(testdir)
# 文件重命名
with open('test.txt', 'w') as f:
    f.write('hello world')
with open('test.py', 'r') as f:
    for line in f.readlines():
        print line.strip()
# os.rename('test.txt', 'test.py')
# 删除文件
