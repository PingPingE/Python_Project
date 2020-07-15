import sqlite3

conn = splite3.connect("example.db")
c = conn.cursor()

# symbol = "RHAT"
# c.execute(''' select * from stocks where symbol='%s'''%symbol)
items = [
    ('2020-07-09','BUY','IBM',100.0,90.0),
    ('2020-07-10','SELL','RHAT',500.0,72.0),
    ('2020-07-11','BUY','IBM',800.0,53.0),
    ('2020-07-12','SELL','RHAT',100.0,90.0)
]
sql = "insert into stocks values(?,?,?,?,?)"
c.executemany(sql,items)
conn.close()