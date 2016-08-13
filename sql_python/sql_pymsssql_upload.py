import pymssql
import sys
import csv
host = 'localhost'
user = 'sa'
password = '1234'
database = 'my project'
try:
    conn = pymssql.connect(host=host, user=user, password=password, database=database, charset='UTF-8')
    cur = conn.cursor()
    result =[]
    writer = csv.reader(open('D:/test_2.csv', 'r'))
    for line in writer:
        result.append(tuple(line))
    #新建数据库
    sql_1 = u"create table item_2_test(id int,review text)"
    cur.execute(sql_1)
    conn.commit()

    #插入数据
    sql_2 = u"insert into item_2_test(id,review) values(%d,%s)"
    cur.executemany(sql_2, result)
    conn.commit()

    print('写进数据库成功!!')
except:
    print(u'写进数据库失败!!')
    print(sys.exc_info()[1])

# 关闭连接
finally:
    conn.close()