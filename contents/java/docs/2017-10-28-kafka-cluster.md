---
layout: post
title: "Kafka集群"
date: 2017-10-28 08:21:49
categories: Java
tags: Java
---


官方文档：<http://kafka.apache.org/0101/documentation.html>

# 软件环境

Linux服务器

已经搭建好的zookeeper集群

kafa_2.9.2-0.8.1.1

# 搭建步骤

kafka依赖zookeeper，虽然kafka安装包中有zookeeper，但是推荐使用独立的zookeeper集群

## 安装配置kafka

```shell
mkdir -p /opt/archives/kafka
tar -xzvf kafka_2.9.2-0.8.1.tgz -C /opt/archives/kafka/
mkdir /opt/kafkalogs
ln -s /opt/archives/kafka/kafka_2.9.2-0.8.1/ /opt/kafka

```

## 配置

```ini
message.max.bytes=5242880
# 每条消息最大字节数，默认是1000012

default.replication.factor=2
# 默认复制因子，保存消息的副本数，默认1

replica.fetch.max.bytes=5242880
# 取消息的最大字节数，默认1048576

num.io.threads=8 
# 这个是borker进行I/O处理的线程数

log.dirs=/opt/kafkalogs
# 消息存放的目录，这个目录可以配置为","逗号分割的表达式，上面的num.io.threads要大于这个目录的个数这个目录，如果配置多个目录，新创建的topic他把消息持久化的地方是，当前以逗号分割的目录中，那个分区数最少就放那一个

zookeeper.connect=192.168.5.111:2181,192.168.5.112:2181,192.168.5.113:2181
# 设置zookeeper的连接端口

advertised.host.name=192.168.5.111
# 这个参数默认是关闭的，在0.8.1有个bug，DNS解析问题，失败率的问题。

broker.id=0 
# 当前机器在集群中的唯一标识，和zookeeper的myid性质一样
```

```ini
# 配置文件/opt/kafka/config/server.properties
broker.id=0
advertised.host.name=192.168.5.111
port=9092
num.network.threads=2
 
num.io.threads=8
socket.send.buffer.bytes=1048576
socket.receive.buffer.bytes=1048576
socket.request.max.bytes=104857600
log.dirs=/opt/kafkalogs
num.partitions=2
log.retention.hours=168
log.segment.bytes=536870912
log.retention.check.interval.ms=60000
log.cleaner.enable=false
zookeeper.connect=192.168.5.111:2181,192.168.5.112:2181,192.168.5.113:2181
zookeeper.connection.timeout.ms=1000000

message.max.bytes=5242880
default.replication.factor=2
replica.fetch.max.bytes=5242880
```

## 启动

```shell
/opt/kafka/bin/kafka-server-start.sh -daemon config/server.properties
```

## 测试

```shell
cd /opt/kafka/
#创建topic
bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 2 --partitions 1 --topic test

#查看topic列表
bin/kafka-topics.sh --list --zookeeper localhost:2181

#查看单个topic信息

#创建consumer，用来接收消息
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning

#创建producer，用来发送消息
bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test

#查看主题信息
bin/kafka-topics.sh --describe --zookeeper localhost:2181 --topic test




zkCli.sh -server localhost:2181
ls /
ls /brokers/ids
get /brokers/ids/1

```



