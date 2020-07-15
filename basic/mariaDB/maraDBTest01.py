import pymysql
conn = pymysql.connect(host='localhost', user='root',password ='root', db='test', 
                        charset='utf8', cursorclass=pymysql.cursors.DictCursor)
c = conn.cursor()
# sql = '''
#     create table if not exists stocks(
#         data text,
#         trans text,
#         symbol text,
#         qty real,
#         price real
#     )
#     '''

c.execute("insert into stocks values('hi','BUY','IBM',100.0,90.0)")
conn.commit()
conn.close()