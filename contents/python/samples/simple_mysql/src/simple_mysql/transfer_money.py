# coding: utf8

import sys

import MySQLdb

class TransferMoney(object):
    
    def __init__(self, conn):
        self.conn = conn

    
    def check_acct_available(self, accid):
        try:
            cursor = self.conn.cursor()
            sql = 'select * from account where accid = %s' % accid
            cursor.execute(sql)
            print 'check_acct_available:', sql
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception('账号%s不存在' % accid)
        finally:
            cursor.close()
        
    
    
    def has_enough_money(self, accid, money):
        try:
            cursor = self.conn.cursor()
            sql = 'select * from account where accid = %s and money > %s' % (accid, money)
            cursor.execute(sql)
            print 'has_enough_money:', sql
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception('账号%s没有足够的钱' % accid)
        finally:
            cursor.close()
    
    
    def reduce_money(self, accid, money):
        try:
            cursor = self.conn.cursor()
            sql = 'update account set money = money - %s where accid = %s' % (money, accid)
            cursor.execute(sql)
            print 'reduce_money:', sql
            if cursor.rowcount != 1:
                raise Exception('账号%减款失败' % accid)
        finally:
            cursor.close()
    
    
    def add_money(self, accid, money):
        try:
            cursor = self.conn.cursor()
            sql = 'update account set money = money + %s where accid = %s' % (money, accid)
            cursor.execute(sql)
            print 'add_money:', sql
            if cursor.rowcount != 1:
                raise Exception('账号%加款失败' % accid)
        finally:
            cursor.close()
        
    
    def transfer(self, source_accid, target_accid, money):
        try:
            self.check_acct_available(source_accid)
            self.check_acct_available(target_accid)
            self.has_enough_money(source_accid, money)
            self.reduce_money(source_accid, money)
            self.add_money(target_accid, money)
            self.conn.commit()
        except Exception as e:
            # print str(e)
            self.conn.rollback()
            raise e
    

if __name__ == '__main__':
    source_accid = sys.argv[1]
    target_accid = sys.argv[2]
    money = sys.argv[3]
    
    conn = MySQLdb.Connect(host='192.168.5.142', port=3376, user='root1', passwd='123456', db='test')
    tr_money = TransferMoney(conn)
    
    try:
        tr_money.transfer(source_accid, target_accid, money)
    except Exception as e:
        print '出现问题：' + str(e)
    finally:
        conn.close()
