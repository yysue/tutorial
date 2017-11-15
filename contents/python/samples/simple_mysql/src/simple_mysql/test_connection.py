import MySQLdb

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

print conn
print cursor

cursor.close()
conn.close()
