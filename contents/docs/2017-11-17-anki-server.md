---
layout: post
title: "Anki自建服务器"
date: 2017-11-17 08:21:49
categories: Anki
tags: Anki
---

未整理


```shell
easy_install AnkiServer
easy_install -i https://pypi.douban.com/simple AnkiServer
easy_install -i https://pypi.douban.com/simple AnkiServer
easy_install -i https://mirrors.ustc.edu.cn/pypi/web/simple AnkiServer

mkdir -p /server/anki

groupadd anki
useradd -g anki -s /sbin/nologin -M anki

下载源码包AnkiServer-2.0.6.tar.gz，并解压
找到如下两个文件
example.ini
supervisor-anki-server.conf
将example.ini重命名为production.ini
将这两个文件复制到/usr/anki目录下
修改production.ini文件
host = 192.168.0.100 #服务器的地址
allowed_hosts = 192.168.0.30,192.168.0.40 #允许同步的客户端ip地址，你也可以写0.0.0.0 允许任何ip地址连

# 向anki服务器中添加一个用户，并设置密码
ankiserverctl.py adduser linuxgirl

# 配置防火墙
firewall-cmd --list-all
firewall-cmd --permanent --add-port=3389/tcp
firewall-cmd --reload

# 测试运行
ankiserverctl.py debug

# 正式运行
ankiserverctl.py start

# 执行以下命令要切换到Anki目录下
ankiserverctl.py debug
ankiserverctl.py start

ankiserverctl.py adduser linuxgirl
ankiserverctl.py deluser linuxgirl
ankiserverctl.py --help
ankiserverctl.py stop

```

