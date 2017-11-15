import MySQLdb
from _sqlite3 import sqlite_version

host = '192.168.5.142'
port = 3376
user = 'root1'
passwd = '123456'
db = 'test'
charset = 'utf8'

conn = MySQLdb.Connect(
    host=host,
    port=port,
    user=user,
    passwd=passwd,
    db=db,
    charset=charset
    )

# conn = MySQLdb.connect(host, user, passwd, db)

cursor = conn.cursor()

sql = 'select * from user'
cursor.execute(sql)

print cursor.rowcount

rs = cursor.fetchone()
print rs

rs = cursor.fetchmany(3)
print rs

rs = cursor.fetchall()
print rs


cursor.close()
conn.close()


