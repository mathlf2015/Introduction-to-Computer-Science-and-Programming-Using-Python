import pymssql
import sys
import csv
host = '192.168.7.252'
user = 'sa'
password = 'i2mago'
database = 'ModelFile'

try:
    conn = pymssql.connect(host = host,user=user,database=database,password=password,charset ='UTF-8')
    cur =conn.cursor()
    sql_1 = 'select * from ConcernsWordNounV4'
    cur.execute(sql_1)
    rows = cur.fetchall()
    conn.commit()
    writer = csv.writer(open('D:/project_review/concernwords_3.csv','w'),lineterminator='\n')
    for row in rows:
        writer.writerow(row)
        print(row)
except:
    print('数据下载失败')
    print(sys.exc_info()[1])
finally:
    conn.close()
