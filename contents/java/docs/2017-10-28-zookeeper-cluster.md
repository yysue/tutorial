Zookeeper集群搭建

官网 http://zookeeper.apache.org

zk官方文档 https://zookeeper.apache.org/doc/r3.4.6/zookeeperAdmin.html



# 软件环境

Linux服务器一台、三台、五台(2*n+1台)

jdk1.7

zookeeper3.4.6

# 搭建步骤

## 安装并配置JDK

```shell
mkdir -p /opt/archives/jdk
tar -xzv -f jdk-7u80-linux-x64.tar.gz -C /opt/archives/jdk/
ln -s /opt/archives/jdk/jdk1.7.0_80/ /opt/jdk

vi ~/.bashrc
# /etc/profile
# 在文件结尾加上这三行
JAVA_HOME=/opt/jdk
CLASSPATH=.:$JAVA_HOME/lib
export PATH=$JAVA_HOME/bin:$PATH

source ~/.bashrc
java -version
javac -version
```



## 安装并配置Zookeeper

### 解压安装 

```shell
mkdir -p /opt/archives/zookeeper
tar -xzv -f zookeeper-3.4.6.tar.gz -C /opt/archives/zookeeper/
ln -s /opt/archives/zookeeper/zookeeper-3.4.6/ /opt/zookeeper

# 创建要用到的目录
cd /opt
mkdir zkdata
mkdir zkdatalog

# 创建标识文件
cd /opt/zkdata
echo 1 >myid # 其他两台分别是2 3
```

### 修改配置文件

```ini
# 修改配置文件
cd /opt/zookeeper/conf
cp zoo_sample.cfg zoo.cfg
vi zoo.cfg
# 修改配置如下所示

# /opt/zookeeper/conf/zoo.cfg配置文件
tickTime=2000
initLimit=10
syncLimit=5
dataDir=/opt/zkdata
dataLogDir=/opt/zkdatalog
clientPort=2181

server.1=192.168.5.111:2888:3888
server.2=192.168.5.112:2888:3888
server.3=192.168.5.113:2888:3888

autopurge.snapRetainCount=66
autopurge.purgeInterval=24
```

### 测试zookeeper

```shell
# 启动/查看/关闭
/opt/zookeeper/bin/zkServer.sh start
/opt/zookeeper/bin/zkServer.sh status
/opt/zookeeper/bin/zkServer.sh stop

# 每台zookeeper都起来，查看status，可以看到两个follower一个leader
# 可用jps查看进程
```

## 注意

### 清理事务日志和快照日志

```shell
# https://zookeeper.apache.org/doc/r3.4.6/zookeeperAdmin.html 
# <dataDir> /opt/zkdata
# <snapDir> /opt/zkdatalog
# <count> 30
java -cp zookeeper.jar:lib/slf4j-api-1.6.1.jar:lib/slf4j-log4j12-1.6.1.jar:lib/log4j-1.2.15.jar:conf org.apache.zookeeper.server.PurgeTxnLog /opt/zkdata /opt/zkdatalog -n 30
# 保存到/server/scripts/zk_clean.sh

#添加定时任务
0 1 * * * 
```

# 配置文件

myid

zoo.cfg

log4j.properties

zkEnv.sh

zkServer.sh

