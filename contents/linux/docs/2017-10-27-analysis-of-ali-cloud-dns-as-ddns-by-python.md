# 通过python将阿里云DNS解析作为DDNS使用



**脚本需要Python2.x运行**



**安装alidns python dsk**

```shell
pip install aliyun-python-sdk-alidns
```



**准备以下数据**

access_key_id：

access_Key_secret：

account_id：可以在你账户的 账号管理 >> 安全设置 中找到；

rc_record_id：你需要先将 i_dont_know_record_id = ‘no’ 设为yes，然后运行脚本，在返还的内容中找到RecordId，这个就是了。获取到RecordId后还需要把i_dont_know_record_id设为no！

rc_domain：一级域名（你的域名）

rc_rr：请填写你的解析记录，对应的主机记录

rc_type：A，CNAME

rc_ttl：请填写解析有效生存时间TTL，单位：秒



**脚本**

[aliyun_ddns.py](https://gitee.com/yysue/tutorial/blob/master/linux/scripts/aliyun_ddns.py)

**获取外网IP**

```shell
curl -s ip.cn

curl -s http://ip.taobao.com/service/getIpInfo2.php?ip=myip|grep -Po '(?<="ip":")\S+(?=")'
```



**设置定时任务**

```shell
crontab -l
*/10 * * * * root /usr/bin/python2.7 /usr/local/shell/aliyun_ddns.py > /dev/null 1>/dev/null
```



阿里云9折优惠码：nfasn1

参考：[通过python将阿里云DNS解析作为DDNS使用](https://enginx.cn/2016/08/22/%E9%80%9A%E8%BF%87python%E5%B0%86%E9%98%BF%E9%87%8C%E4%BA%91dns%E8%A7%A3%E6%9E%90%E4%BD%9C%E4%B8%BAddns%E4%BD%BF%E7%94%A8.html)

