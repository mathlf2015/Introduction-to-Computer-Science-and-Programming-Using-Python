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
    writer = csv.reader(open('D:/result_1.csv', 'r'))
    for line in writer:
        result.append(tuple(line))
    #新建数据库
    sql_1 = u"create table result_1(pos_sum float,neg_sum float,pos_mean float,neg_mean float,pos_std float,neg_std float)"
    cur.execute(sql_1)
    conn.commit()

    #插入数据
    sql_2 = u"insert into result_1(pos_sum ,neg_sum ,pos_mean ,neg_mean ,pos_std ,neg_std ) values(%d,%d,%d,%d,%d,%d)"
    cur.executemany(sql_2, result)
    conn.commit()

    print('写进数据库成功!!')
except:
    print(u'写进数据库失败!!')
    print(sys.exc_info()[1])

    # 关闭连接
finally:
    conn.close()