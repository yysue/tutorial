# python软件包安装和开发工具

# Python版本

```shell
python --version
```

# Python软件包安装

## 手动安装

下载

```shell
wget http://xael.org/pages/python-nmap-0.6.0.tar.gz
```
解压
```shell
tar -xzvf python-nmap-0.6.0.tar.gz
cd python-nmap-0.6.0
```
安装
```shell
python setup.py install
```

## easy_install安装

easy_install是Python setuptools组件中的一个模块

```shell
apt-get install python-setuptools
```

使用easy_install安装另一个模块

```shell
easy_install pyPdf
```

## pip安装

安装pip

```shell
apt-get install python-pip
```

通过pip安装github3

```shell
pip install github3.py
```

# 开发工具

## sublime text

## eclipse + pydev

## vscode

## Aptana Studio

[Aptana Studio](http://www.aptana.com/)

## WingIDE(推荐这个)

下载

```shell
wget http://wingware.com/pub/wingide/5.1.11/wingide5_5.1.11-1_amd64.deb
```

安装

```shell
dpkg -i wingide5_5.1.11-1_amd64.deb
```
