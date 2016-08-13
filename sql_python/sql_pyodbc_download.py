import pyodbc
import pandas as pd
from pandas import Series,DataFrame
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.7.252;PORT=1433;DATABASE=ModelFile;UID=sa;PWD=i2mago')
cursor = cnxn.cursor()
#df = cursor.execute("select * from BuyersReview")
#cursor.execute("insert into datatest(a, b) values ('你好', '世界')")
#print(df)
#cnxn.commit()
cursor.execute("select * from ConcernsWordNounV4")
rows = cursor.fetchall()
#for row in rows:
#    print (row)
print(len(rows))
print(cursor.description)
import numpy as np
rows = np.array(rows).reshape(len(rows),len(rows[0]))
df = DataFrame(rows,columns=[i[0] for i in cursor.description])
#print([i[0] for i in cursor.description])
df.to_csv('D:/project_review/concernwords_2.csv',index=None,encoding='gbk')
print(df.head())
cnxn.commit()

'''cnxn_1 = pyodbc.connect(
    DRIVER='{SQL SERVER NATIVE CLIENT 10.0}',
    SERVER='localhost',
    DATABASE='df1',
    uid='sa',
    pwd='1234')
cursor_1 = cnxn_1.cursor()
#(('keyWord', <class 'str'>), ('productID', <class 'str'>), ('review', <class 'str'>), ('reviewDate', <class 'str'>, ), ('appendReviewTag', <class 'int'>, ), ('sku', <class 'str'>, ), ('reviewNO', <class 'int'>, ), ('saveDate', <class 'str'>, ), ('segmentation', <class 'str'>, ), ('word', <class 'str'>, ), ('productNO', <class 'int'>, ), ('type', <class 'str'>,))
cursor_1.execute("create table datatest2(cursor.description)")
#cursor_1.executemany("""INSERT INTO datatest2 VALUES (?, ?,?,?,?,?,?,?,?,?,?,?)""",rows)
cnxn_1.commit()'''


