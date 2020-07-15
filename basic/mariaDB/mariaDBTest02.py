import pymysql
conn = pymysql.connect(host='localhost', user='root',password ='root', db='test', 
                        charset='utf8', cursorclass=pymysql.cursors.DictCursor)
c = conn.cursor()
t =('ibm',)
sql = 'select * from stocks where symbol = %s'
c.execute(sql, t)
print(c.fetchall())

# items = [
#     ('2020-07-09','BUY','IBM',100.0,90.0),
#     ('2020-07-10','SELL','RHAT',500.0,72.0),
#     ('2020-07-11','BUY','IBM',800.0,53.0),
#     ('2020-07-12','SELL','RHAT',100.0,90.0)
# ]
# sql = "insert into stocks values(%s,%s,%s,%s,%s)"
# c.executemany(sql, items)
# conn.commit()
c.close()
conn.close()