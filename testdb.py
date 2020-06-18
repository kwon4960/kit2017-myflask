import sqlite3
conn = sqlite3.connect('mydb.db')

# cursor 객체 생성
c = conn.cursor()

num = ('20201235',)
c.execute('SELECT * FROM student WHERE num = ?', num)
print(c.fetchone())

# 접속한 db 닫기
conn.close() 