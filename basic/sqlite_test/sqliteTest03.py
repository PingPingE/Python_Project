import sqlite3,csv
input_file = 'input.csv'
conn = sqlite3.connect('supplier.db')
c = conn.cursor()
# sql = '''create table if not exists suppliers(
#     supplier_name varchar(20),
#     invoice_number varchar(20),
#     part_number varchar(20),
#     cost_float,
#     purchase_date date
# )'''

sql = 'delete from suppliers'
c.execute(sql)
conn.commit()

file_reader = csv.reader(open(input_file,'r'), delimiter=',')
header = next(file_reader, None)
print(type(file_reader))
print(header)
data = []
for row in file_reader:
    print(type(row))
    data.append(row)

sql = 'insert into suppliers values(?,?,?,?,?)'
c.executemany(sql, data)
conn.commit()
c.close()
conn.close()