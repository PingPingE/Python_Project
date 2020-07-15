import cx_Oracle

class OracleClass():
    def __init__(self, dataB):
        self.conn = cx_Oracle.connect(dataB)
        self.c = self.conn.cursor()
        print(self.conn.version)
    
    def create_table(self, sql):
        self.c.execute(sql)
        self.conn.commit()

    def create_sequence(self, name):
        self.c.execute(f'create sequence {name} start with 1 increment by 1')
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

ora = OracleClass('hr/hr@localhost:1521/xe')

# ora.create_table('''
# create table books(
#     book_id number not null,
#     title varchar2(50),
#     published_date varchar2(50),
#     publisher varchar2(50),
#     pages number,
#     recommend number,
#     constraint pk_book primary key(book_id))
# ''')
#ora.create_sequence('book_seq')
items = [
    ('flower','2020-07-09','one',210,100),
    ('star','2020-07-09','two',300,10),
    ('good morning','2020-07-09','three',800,53)
]
sql = 'insert into books values(book_seq.nextval,:1,:2,:3,:4,:5)'
ora.insert(sql, items)
ora.select('select * from books')
ora.close()