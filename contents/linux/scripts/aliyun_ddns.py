# -*- coding: UTF-8 -*-
 
import json
import os
import re
import sys
from datetime import datetime
 
from aliyunsdkalidns.request.v20150109 import UpdateDomainRecordRequest, DescribeDomainRecordsRequest, \
    DescribeDomainRecordInfoRequest
from aliyunsdkcore import client
 
#请填写你的Access Key ID
access_key_id = ""
 
#请填写你的Access Key Secret
access_key_secret = ""
 
#请填写你的账号ID
account_id = ""
 
#如果选择yes，则运行程序后仅现实域名信息，并不会更新记录，用于获取解析记录ID。
#如果选择no，则运行程序后不显示域名信息，仅更新记录
i_dont_know_record_id = 'no'
 
#请填写你的一级域名
rc_domain = ''
 
#请填写你的解析记录,对应的主机记录
rc_rr = ''
 
#请填写你的记录类型，DDNS请填写A，表示A记录
rc_type = 'A'
 
#请填写解析记录ID
rc_record_id = ''
 
#请填写解析有效生存时间TTL，单位：秒
#rc_ttl = '1'
rc_ttl = '600'
 
#请填写返还内容格式，json，xml
rc_format = 'json'
 
 
def my_ip():
    get_ip_method = os.popen('curl -s ip.cn')
    get_ip_responses = get_ip_method.readlines()[0]
    get_ip_pattern = re.compile(r'\d+\.\d+\.\d+\.\d+')
    get_ip_value = get_ip_pattern.findall(get_ip_responses)[0]
    return get_ip_value
 
 
def check_records(dns_domain):
    clt = client.AcsClient(access_key_id, access_key_secret, 'cn-hangzhou')
    request = DescribeDomainRecordsRequest.DescribeDomainRecordsRequest()
    request.set_DomainName(dns_domain)
    request.set_accept_format(rc_format)
    #result = clt.do_action(request)
    result = clt.do_action_with_exception(request)
    return result
 
 
def old_ip():
    clt = client.AcsClient(access_key_id, access_key_secret, 'cn-hangzhou')
    request = DescribeDomainRecordInfoRequest.DescribeDomainRecordInfoRequest()
    request.set_RecordId(rc_record_id)
    request.set_accept_format(rc_format)
    #result = clt.do_action(request)
    result = clt.do_action_with_exception(request)
    result = json.JSONDecoder().decode(result)
    result = result['Value']
    return result
 
 
def update_dns(dns_rr, dns_type, dns_value, dns_record_id, dns_ttl, dns_format):
    clt = client.AcsClient(access_key_id, access_key_secret, 'cn-hangzhou')
    request = UpdateDomainRecordRequest.UpdateDomainRecordRequest()
    request.set_RR(dns_rr)
    request.set_Type(dns_type)
    request.set_Value(dns_value)
    request.set_RecordId(dns_record_id)
    request.set_TTL(dns_ttl)
    request.set_accept_format(dns_format)
    #result = clt.do_action(request)
    result = clt.do_action_with_exception(request)
    return result
 
def write_to_file():
    time_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    current_script_path = sys.path[7]
    print current_script_path
    log_file = current_script_path + '/' + 'aliyun_ddns_log.txt'
    write = open(log_file, 'a')
    write.write(time_now + ' ' + str(rc_value) + '\n')
    write.close()
    return
 
if i_dont_know_record_id == 'yes':
    print check_records(rc_domain)
elif i_dont_know_record_id == 'no':
    rc_value = my_ip()
    rc_value_old = old_ip()
    if rc_value_old == rc_value:
        print 'The specified value of parameter Value is the same as old'
    else:
        print update_dns(rc_rr, rc_type, rc_value, rc_record_id, rc_ttl, rc_format)
        write_to_file()
