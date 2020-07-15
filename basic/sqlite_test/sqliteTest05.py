import sqlite3
class sqliteClass():
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.c = self.conn.cursor()
    
    def create_table(self, sql):
        self.c.execute(sql)
        self.conn.commit()

    def insert(self, sql, items):
        self.c.executemany(sql, items)
        self.conn.commit()
    
    def delete(self, sql, items):
        if len(items)>0:
            self.c.executemany(sql, items)
        else:
            self.c.execute(sql)
        self.conn.commit()
        
    def select(self, sql, items):
        if len(items) >0:
            print(list(i for i in self.c.executemany(sql,items)))
        else:
            print(list(i for i in self.c.execute(sql)))


    def update(self, sql):
        self.c.executemany()

    def close(self):
        self.c.close()
        self.conn.close()

target = sqliteClass('example.db')
target.select('select * from stocks',[])
