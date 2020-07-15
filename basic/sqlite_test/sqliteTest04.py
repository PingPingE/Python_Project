import sqlite3
def create_table():
    conn = splite3.connect()
    c = conn.cursor()
    c.execute('''
            create table books(
                title text, 
                published date, 
                publisher text, 
                qty real, 
                price real)''')

    conn.commit()
    c.close()
    conn.close()

def insert_books(items):
    conn = sqlite3.connect()
    c= conn.cursor()
    sql = 'insert into books values(?,?,?,?,?)'
    c.executemany(sql, items)
    conn.commit()
    c.close()
    conn.close()

create_table()
items = [('데이터분석실무','2020-07-10','위키북스',300,10),
    ('데이터분석','2020-07-11','위키북스스슷',400,10),
    ('데분','2020-07-12','위키키키북스',500,10)]
insert_books(items)
