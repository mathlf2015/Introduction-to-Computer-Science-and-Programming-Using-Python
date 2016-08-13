import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
import json
db = json.load(open(r'E:\git_download\pydata-book\ch07\foods-2011-10-03.json'))
info_keys = ['description', 'group', 'id', 'manufacturer']
info = DataFrame(db, columns=info_keys)
nutrients = []
for rec in db:
    fnuts = DataFrame(rec['nutrients'])
    fnuts['id'] = rec['id']
    nutrients.append(fnuts)
#print(nutrients[:2])
nutrients = pd.concat(nutrients, ignore_index=True)
#去除重复项
nutrients = nutrients.drop_duplicates()
#修改重复的名字
col_mapping = {'description' : 'food',
               'group'       : 'fgroup'}
info = info.rename(columns=col_mapping, copy=False)
col_mapping = {'description' : 'nutrient',
               'group' : 'nutgroup'}
nutrients = nutrients.rename(columns=col_mapping, copy=False)
ndata = pd.merge(nutrients, info, on='id', how='outer')

#中位点图像
result = ndata.groupby(['nutrient', 'fgroup'])['value'].quantile(0.5)
result['Zinc, Zn'].sort_values().plot(kind='barh')
plt.show()
print(result.head())
by_nutrient = ndata.groupby(['nutgroup', 'nutrient'])
get_maximum = lambda x: x.xs(x.value.idxmax())
get_minimum = lambda x: x.xs(x.value.idxmin())
max_foods = by_nutrient.apply(get_maximum)[['value', 'food']]
print(max_foods.head())
# make the food a little smaller
max_foods.food = max_foods.food.str[:50]
print(max_foods.ix['Amino Acids']['food'])
