import pyodbc

import pyodbc
import csv
cnxn = pyodbc.connect(
            DRIVER='{SQL SERVER NATIVE CLIENT 10.0}',
            SERVER='localhost',
            DATABASE='my project',
            uid='sa',
            pwd='1234')

cursor = cnxn.cursor()
cursor.execute("create table result_1(pos_sum float,neg_sum float,pos_mean float,neg_mean float,pos_std float,neg_std float)")
writer = csv.reader(open('D:/result_1.csv','r'))
for line in writer:
    cursor.execute("INSERT INTO result_1(pos_sum ,neg_sum ,pos_mean ,neg_mean ,pos_std ,neg_std ) VALUES(?, ?,?,?,?,?)" ,line)
    cnxn.commit()

'''cursor.execute("create table datatest(a text,b text)")
out=(['c','e'],['f','g'])
cursor.execute("""INSERT INTO datatest VALUES
    (?, ?)""",out)

df_test = cursor.execute('select * from datatest')

row = cursor.fetchone()
if row:
    print (row)
cnxn.commit()'''


