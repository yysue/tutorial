import mysql.connector

conn = mysql.connector.connect(host = '192.168.5.142', port = '3376', user = 'root1', password = '123456', database = 'test')
cursor = conn.cursor()

cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
cursor.rowcount

conn.commit()
cursor.close()
conn.close()
