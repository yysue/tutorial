---
layout: post
title: "Windows强制删除文件及文件夹命令"
date: 2017-11-11 08:21:49
categories: Windows
tags: Windows
---

Windows强制删除文件及文件夹命令



**一、删除文件或目录CMD命令：**

rd/s/q 盘符:\某个文件夹  （强制删除文件文件夹和文件夹内所有文件）
del/f/s/q 盘符:\文件名  （强制删除文件，文件名必须加文件后缀名）

**二、删除文件或目录BAT命令：**

1、新建.BAT批处理文件输入如下命令，然后将要删除的文件拖放到批处理文件图标上即可删除。
DEL /F /A /Q 
RD /S /Q 



参考：https://www.cnblogs.com/sinlang5778/articles/2244694.html

