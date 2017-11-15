

Python2.7

# Python DB API

Python DB API：Python访问数据库的统一接口规范

https://www.python.org/dev/peps/pep-0249/

## connection:建立数据库连接

## cursor:执行SQL、获取数据





#  开发数据库程序流程

## Python MySQL开发环境

Python-MySQL connector

https://sourceforge.net/projects/mysql-python/

## 流程

1. 创建connection对象，获取cursor

   >  [test_connection.py](../samples/simple_mysql/src/simple_mysql/test_connection.py)

2. 使用cursor执行SQL

   > 1. [test_cursor.py](../samples/simple_mysql/src/simple_mysql/test_cursor.py)
   > 2. [test_select.py](../samples/simple_mysql/src/simple_mysql/test_select.py)

3. 使用cursor获取数据、判断执行状态

   > [test_iud.py](../samples/simple_mysql/src/simple_mysql/test_iud.py)

4. 提交事务或者回滚事务

5. 关闭curosor、关闭connection

## 一个银行转账的例子

>  [transfer_money.py](../samples/simple_mysql/src/simple_mysql/transfer_money.py)









