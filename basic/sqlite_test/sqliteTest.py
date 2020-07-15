import sqlite3
conn = sqlite3.connect('example.db')
cur = conn.cursor()
# cur.execute('''
#             create table stocks(date text, trans text, 
#             symbol text, qty real, price real)''')
cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
conn.commit()
conn.close()
