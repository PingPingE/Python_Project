import pymysql

class MariaClass():
    def __init__(self, dataB):
        self.conn = pymysql.connect(host='localhost', user='root',password ='root', db=dataB, 
                        charset='utf8', cursorclass=pymysql.cursors.DictCursor)
        self.c = self.conn.cursor()
    
    def create_table(self, sql):
        self.c.execute(sql)
        self.conn.commit()

    def insert(self, sql, items=''):
        if items == '':
            self.c.execute(sql)
        else:
            self.c.executemany(sql, items)
        self.conn.commit()
    
    def delete(self, sql, items=''):
        if items == '':
            self.c.execute(sql)
        else:
            self.c.executemany(sql, items)
        self.conn.commit()
        
    def select(self, sql, items=''):
        if items == '':
            print('------------------select all--------------------')
            self.c.execute(sql)
            print(self.c.fetchall())
        else:
            for i in items:
                self.c.execute(sql,i)
                print(self.c.fetchall())
                
        print('------------------------------------------------')

    def update(self, sql):
        self.c.executemany()

    def close(self):
        self.c.close()
        self.conn.close()


sql = '''
        create table if not exists books(
        book_id integer not null auto_increment primary key,
        title text,
        published_date text,
        publisher text,
        pages integer,
        recommend integer) default charset=utf8;
        
        '''
maria = MariaClass('test')
maria.create_table(sql)
items = [
    ('flower','2020-07-09','one',210,100),
    ('star','2020-07-09','two',300,10),
    ('good morning','2020-07-09','three',800,53)
]
sql = 'insert into books(title, published_date, publisher, pages, recommend) values(%s,%s,%s,%s,%s)'
maria.insert(sql, items)
maria.select('select * from books')
maria.select('select * from books where book_id=%s  ', [[1],[2],[3],[4]])
maria.close()