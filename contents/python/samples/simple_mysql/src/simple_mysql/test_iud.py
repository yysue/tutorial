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

sql_insert = 'insert into user(name) values ("name10")'
sql_update = 'update user set name = "name1" where id = 4'
sql_delete = 'delete from user where d < 3'

try:
    cursor.execute(sql_insert)
    print cursor.rowcount
    cursor.execute(sql_update)
    print cursor.rowcount
    cursor.execute(sql_delete)
    print cursor.rowcount
    
    conn.commit()
except Exception as e:
    print e
    conn.rollback()

cursor.close()
conn.close()
