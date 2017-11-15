import mysql.connector

conn = mysql.connector.connect(host = '192.168.5.142', port = '3376', database = 'test', user = 'root1', password = '123456')
cursor = conn.cursor()

cursor.execute('select * from user;')

values = cursor.fetchall()
print(values)

cursor.close()
conn.close()
