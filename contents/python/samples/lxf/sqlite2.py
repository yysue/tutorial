import sqlite3

conn = sqlite3.connect('/data/test.db')
cursor = conn.cursor()

#cursor.execute('select * from user where id = ?', ('1', ))
cursor.execute('select * from user')
values = cursor.fetchall()
print(values)

cursor.close()
conn.close()
