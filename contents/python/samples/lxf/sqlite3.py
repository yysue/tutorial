import sqlite3

def get_score_in(low, high):
    conn = sqlite3.connect('/data/test.db')
    cursor = conn.cursor()

    #cursor.execute('select * from user where score between ? and ?', (60, 80))
    cursor.execute('select * from user where score between ? and ?', (low, high))
    values = cursor.fetchall()

    #print(values)

    cursor.close()
    conn.close()

    return values

print(get_score_in(80, 95))
print(get_score_in(60, 80))
print(get_score_in(60, 100))
