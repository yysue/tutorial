---
layout: post
title: "MySQL启动方式"
date: 2017-10-02 08:21:49
categories: MySQL
tags: MySQL
---

# 启动方式

##几个问题

1. /etc/init.d/mysql 这个脚本从哪来

2. mysql能否设置成开机启动

3. 有没有必要把MySQL设置为开机启动

   > 如果线上库，建议关闭自动启动
   > 线上库本着一个原则 ，出错了就停下来
   > 用脚本批量启动

4. mysqld可以加载哪些位置的配置文件

   > mysql --help|grep my.cnf
   > mysqld --verbose --help|grep my.cnf
   > mysqld --verbose --help|grep defaults-file
   >
   > 加载顺序：
   > /etc/my.cnf /etc/mysql/my.cnf /usr/local/mysql/etc/my.cnf ~/.my.cnf 



```shell
/etc/init.d/mysql start (mysql.server)
/usr/local/mysql/bin/mysqld_safe --defaults-file=/etc/my.cnf &
/usr/local/mysql/bin/mysqld --defaults-file=/etc/my.cnf &

mysql.servery调用的mysqld_safe
mysqld_safe调用的mysqld (mysqld_safe是mysqld的守护进程，会自动重启)

# 建议用如下启动方式，一机多实例启动也就简单了
# mysqld_safe启动，mysqld进程挂掉，会自动重启，不便于定位问题
/usr/local/mysql/bin/mysqld --defaults-file=/etc/my.cnf &
/usr/local/mysql/bin/mysqld --defaults-file=/data/mysql/mysql3376/my3376.cnf &
/usr/local/mysql/bin/mysqld --defaults-file=/data/mysql/mysql3377/my3377.cnf &

# 关闭
/usr/local/mysql/bin/mysqladimn -S /tmp/mysql3376.sock shutdown
```

## 为什么用mysqld启动

1. 一机多实例启动也就简单了
2. mysqld_safe启动，mysqld进程挂掉，会自动重启，不便于定位问题

> 一机多实例场景：
>
> 一机多实例技巧：
> 一组MySQL用一个唯一端口号，所以组之间不会重复

## 一机多实例实现

```shell
1. 创建目录
mkdir -p /data/mysql/mysql3377/{data,tmp,logs}

2. 修改配置文件，端口
# cp /data/mysql/mysql3376/mysql3376.cnf /data/mysql/mysql3377/mysql3377.cnf
cp /etc/my.cnf /data/mysql/mysql3377/mysql3377.cnf
sed -i 's/3376/3377/g' /data/mysql/mysql3377/mysql3377.cnf

3. 修改权限
sudo chown -R mysql:mysql /data/mysql/mysql3377

4. 初始化，指定配置文件
cd /usr/local/mysql
./scripts/mysql_install_db --defaults-file=/data/mysql/mysql3377/mysql3377.cnf

5. 通过mysqld启动
mysqld --defaults-file=/data/mysql/mysql3377/mysql3377.cnf &

6. 安全加固
mysql -S /tmp/mysql3377.sock

7. 关闭
mysqladimn -S /tmp/mysql3377.sock shutdown

port, bp size, appname
$appname$port
```

## mysqld_multi

1. mysqld_multi可以调用mysqld_safe，也可以调用mysqld
2. 如果mysqld_multi，建议调用mysqld_safe
3. my.cnf必须在/etc/my.cnf这个位置
4. http://www.cnblogs.com/LCX/archive/2010/04/02/1703215.html

**向my.cnf追加如下内容**

> [mysqldN]会覆盖[mysqld]的部分
> port/datadir/socket必须不能一样

```shell
[mysqld_multi]
mysqld  = /usr/local/mysql/bin/mysqld_safe
mysqladmin = /usr/local/mysql/bin/mysqladmin
user  = root
password    = 123456
#log  = /usr/local/mysql/etc/mysqld_multi.log

# cat /usr/local/mysql/etc/mysqld_multi.cnf 
[mysqld3376]
socket  = /tmp/mysql3376.sock
port  = 3376
# pid-file  = /usr/local/mysql/var1/localhost.pid
datadir=/data/mysql/mysql3376
user  = mysql
 
[mysqld3377]
socket          = /tmp/mysql3377.sock
port            = 3377
#pid-file        = /usr/local/mysql/var2/localhost.pid
datadir=/data/mysql/mysql3377
user            = mysql
```

**启动**

```shell
# 查看MySQL状态
/usr/local/mysql/bin/mysqld_multi report

# 启动，不加参数是启动所有实例
/usr/local/mysql/bin/mysqld_multi start
# 只启动3376
/usr/local/mysql/bin/mysqld_multi start 3376

# 关闭，这个也只可以加参数
mysqld_multi stop
mysqladmin shutdown -S /tmp/mysql3376.sock
```

## 打包初始化

```shell
/data/mysql/mysql3376
# 打包前，删除auto.cnf
rm -rf /data/mysql/mysql3376/auto.cnf
tar -czvf mysqldata.tar.gz /data/mysql/mysql3376
```



# 故障排查

1. 看错误日志

   ```shell
   cat /data/mysql/mysql3376/logs/error.log
   ```

## 常见错误

1. 字典数据过大

   ```shell
   # 数据字典文件
   innodb_data_file_path=ibdata1:100M:autoextend
   ```

2. ibdata1非常大，怎么办？

   > 很有可能是启用了共享表空间，改成独立表空间
   > 共享表空间，就是把数据清理掉后，也不会回收空间
   >
   > 解决：
   >
   > 1. dump出来
   > 2. 启用独立表空间导入vi

3. 优化错误

   ```shell
   [mysqld_safe]
   malloc-lib = /usr/local/mysql/lib/mysql/libjemalloc.so
   ```

   > 用/etc/init.d/mysql和mysqld_safe启，连错误日志都没有写
   > 错误日志是由mysqld来写的，所以连mysqld都没有调用到
   >
   > 解决：
   >
   > 1. 把缺少的文件找来编译放进去
   > 2. 把这句优化注释掉

## 总结

> **问题来源：**
> 目录权限问题
> 优化问题
>
> **解决思路：**
> 看调用关系
> 看日志

# 要求

1. 能按着要求布署一个数据库3378
2. 了解几种启动方式的调用关系
3. 了解配置文件加载的顺序
4. 掌握启动故障的排查思路
5. 多实例的布署


# BUG

https://bugs.mysql.com/bug.php?id=84427

> 设置error_log必须提前创建好






