import pyodbc
import pandas as pd
from pandas import Series,DataFrame
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;PORT=1433;DATABASE=df1;UID=sa;PWD=1234')
cursor = cnxn.cursor()
table_name_set = ['BuyersConcernsReviewCut',
                  'BuyersConcernsReviewCut234',
                  'BuyersConcernsReviewCut234Se',
                  'BuyersConcernsReviewCutNoun_ADJ1234_WithoutSeg',
                  'BuyersConcernsReviewCutNoun_ADJ1234_WithSeg',
                  'BuyReview',
                  'BuyReviewCut',
                  'ConcernsWordADJ',
                  'ConcernsWordADJ234',
                  'ConcernsWordWhole',
                  'ConcernsWordWholeCheckPOS',
                  'ConcernsWordWholeNoun']
order_set = ["select * from {}".format(str(i)) for i in table_name_set]
save_set = ['D:/project_review/{}.csv'.format(str(i)) for i in table_name_set]
#print(save_set)
def download_data(order_set,save_set):
    for i in range(len(table_name_set)):
        cursor.execute(order_set[i])
        rows = cursor.fetchall()
        #print(len(rows))
        #print(cursor.description)
        import numpy as np
        rows = np.array(rows).reshape(len(rows),len(rows[0]))
        df = DataFrame(rows,columns=[i[0] for i in cursor.description])
        #print([i[0] for i in cursor.description])
        df.to_csv(save_set[i],index=None,encoding='GB2312')
        print(df.head())
        cnxn.commit()

download_data(order_set,save_set)