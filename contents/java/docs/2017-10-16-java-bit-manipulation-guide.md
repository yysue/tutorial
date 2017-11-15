---
layout: post
title:  "Java二进制操作指南"
date:   2017-10-16 08:21:49
categories: Java
tags: Java
---

# 移位

位运算中大多数操作都是向左移位和向右移位。在Java中，这对应着<<和>>这两个操作符，示例如下：

```java
/* 00000001 << 1 = 00000010 */
1 << 1 == 2 
 
/* 00000001 << 3 = 00001000 */
1 << 3 == 8
 
/* 11111111 11111111 11111111 11110000 >> 4 = 11111111 11111111 11111111 11111111 */
0xFFFFFFF0 >> 4 == 0xFFFFFFFF 
 
/* 00001111 11111111 11111111 11111111 >> 4 = 00000000 11111111 11111111 11111111 */
0x0FFFFFFF >> 4 == 0x00FFFFFF
```

**注意：** 向右移位是有符号操作符。和许多语言一样，Java使用最高位来表示数值的正负，负数的最高位永远为1。一个以1开头的二进制数移位后还将以1开头，一个以0开头的二进制树移位后还将以0开头。所以**要小心**：Java是可以在整数中进行位运算的。

你可以使用叫作“无符号右移”运算符的第三个操作符：>>> 来实现以“0”填充的移位，这种移位会忽略符号位并总是用“0”来填充。

```java
/* 10000000 00000000 00000000 00000000 >>> 1 = 01000000 00000000 00000000 00000000 */
0x80000000 >>> 1 == 0x40000000
 
/* 10000000 00000000 00000000 00000000 >> 1 = 11000000 00000000 00000000 00000000 */
0x80000000 >> 1  == 0xC0000000
```

最大的用途之一是迅速求2的幂。1向左移位1位是2，移2位是4，移3位是8…… 相似的，向右移1位相当于是把该数除以2。

另一个用途便是创建掩码。位掩码可用于屏蔽或者修改一个二进制数中的某些指定位，下一部分会进行详细讲解。假如我们想要创建一个
*00001000*的掩码，代码十分简单：

```java
int bitmask = 1 << 3;
```

你可以使用位运算操作符来创建更复杂的掩码，下一部分同样会讲解位运算操作符。

# 位运算操作符

以下是Java中四个常见的位操作符：

- `~` – 按位取反
- `&` – 按位与
- `~` – 按位异或
- `|` – 按位或

简单应用如下（简单起见，只展示二进制）

```java
1010 & 0101 == 0000
1100 & 0110 == 0100
 
1010 | 0101 == 1111
1100 | 0110 == 1110
 
~1111 == 0000
~0011 == 1100
 
1010 ^ 0101 == 1111
1100 ^ 0110 == 1010
```

比如，你可以通过“或”运算，把一个二进制数上的指定位“设置”为1，并且不会影响到其他位。

```java
10000001 | 00100000 = 10100001 /* 第五位设为1 */
10000001 | 1 << 5 = 10100001 /* 同样作用 */
00000000 | 1 << 2 | 1 << 5 = 00100100
```

有些技巧可以让你在写的时候免去分支判断，我就不在这里描述了，你可以[自己看看](http://graphics.stanford.edu/~seander/bithacks.html)。

如果你想要选择性的把某位设为0，你可以让数与一个全1但是某位为0的数相与。

```java
01010101 & ~(1<<2) == 01010101 & 11111011 == 01010001
```

# 关于位顺序

假设最高位是在左边：

```java
10010110
^      ^
|      |------- 第 0 位
|
|-------------- 第 7 位
```

注意，第0位的值是2^0，第一位是2^1，……，第7位的值是2^7。

# 使用ParseInt

在你的代码里操作二进制数字的便利方法是使用*Integer.parseInt()*方法*。Integer.parseInt(“101″,2)*代表着把二进制数101转换为十进制数（5）。这意味着，利用这个方法你甚至可以在for循环里使用二进制数字：

```java
/* 从5到15的循环 */
for (int b = Integer.parseInt("0101",2); b <= Integer.parseInt("1111",2); b++) {
    /* 做些什么 */
}
```

# 位读写

建议：自己实现一个用来把二进制位（**比特**）转换为流并读写的类，尽量不要使用Java的输入输出流，因为Java的流只能按**字节**操作。你会觉得“给我接下来的N个比特”和“把指针往前移M位”这种功能是非常实用的。比如，你可以读取足够的数据来确定最长的霍夫曼编码的长度，当你得到你刚刚读取的霍夫曼编码的实际长度之后，你就可以把指针往前移相应长度。一个这样的类可以把位运算丑陋的一面划分成一个眼熟的代码块。

类似的，如果你追求速度的话，那你会意外的发现表查找是如此强大。假如你有一个霍夫曼编码以0开头，并且其他的编码长度均为3而且以1开头，这意味着你需要一个可以容纳8(2^3)个项的表格，你的表格可能是这样的：

```java
char code[8];
int codelen[8];

code[0] = 'a'; codelen[0] = 1;
code[1] = 'a'; codelen[1] = 1;
code[2] = 'a'; codelen[2] = 1;
code[3] = 'a'; codelen[3] = 1;
code[4] = 'b'; codelen[4] = 3;
code[5] = 'c'; codelen[5] = 3;
code[6] = 'd'; codelen[6] = 3;
code[7] = 'e'; codelen[7] = 3;
```

通过两次查找，你就可以定位到你要找的字符，并且还可以知道下一个字符在前面多少位置。这可要比某些一遍遍的循环去查找全部字符要划算的多，也更节省内存。

*课后作业：用代码实现以上表格的自动生成。想要更刺激的话，允许表格中的比特可变长。如果要查找的字符不在当前表，那就自动往下一个表去找，这是一种空间换时间的办法。*

原文链接： [sys.cs.rice.edu](http://sys.cs.rice.edu/course/comp314/10/p2/javabits.html) 翻译： [ImportNew.com - 吴 鹏煜](http://www.importnew.com/author/nappp)

译文链接： http://www.importnew.com/15060.html

# 举例

1. [Number Complement](https://leetcode.com/problems/number-complement/description/)