import pandas as pd
import numpy as np
from pandas import *
import matplotlib.pyplot as plt


tips = pd.read_csv('E:/mydata/tips.csv')
party_counts = pd.crosstab(tips['day'], tips['size'])
print(party_counts)
# Not many 1- and 6-person parties
party_counts = party_counts.ix[:, 2:5]
# Normalize to sum to 1
party_pcts = party_counts.div(party_counts.sum(1).astype(float), axis=0)
print(party_pcts)

party_pcts.plot(kind='bar', stacked=True)
plt.show()
#直方图，单个属性在各个因子水平上的频率
plt.figure()
tips['tip_pct'] = tips['tip'] / tips['total_bill']
tips['tip_pct'].hist(bins=50)
plt.show()
#kde
plt.figure()
tips['tip_pct'].plot(kind='kde')
plt.show()
#双峰图像
comp1 = np.random.normal(0, 1, size=200)  # N(0, 1)
comp2 = np.random.normal(10, 2, size=200)  # N(10, 4)
values = Series(np.concatenate([comp1, comp2]))
values.hist(bins=100, alpha=0.3, color='k', normed=True)
values.plot(kind='kde', style='k--')

#散点图，观察两个一位序列间的关系
macro = pd.read_csv('E:/mydata/macrodata.csv')
data = macro[['cpi', 'm1', 'tbilrate', 'unemp']]
trans_data = np.log(data).diff().dropna()
trans_data[-5:]
plt.figure()
plt.scatter(trans_data['m1'], trans_data['unemp'])
plt.title('Changes in log %s vs. log %s' % ('m1', 'unemp'))
#创建一组变量的散布图矩阵
pd.scatter_matrix(trans_data, diagonal='kde', color='k', alpha=0.3)
plt.show()

#pandas数据聚合和分组运算
tips = pd.read_csv('E:/mydata/tips.csv')
tips['tip_pct'] = tips['tip'] / tips['total_bill']
def peak_to_peak(arr):
    return arr.max() - arr.min()
print(tips[:6])
#数据聚合
grouped = tips.groupby(['sex', 'smoker'])
grouped_pct = grouped['tip_pct']
print(grouped_pct.agg('mean'))
#函数名作为操作后的列名
print(grouped_pct.agg(['mean', 'std', peak_to_peak]))
#自定义列名
print(grouped_pct.agg([('foo', 'mean'), ('bar', np.std)]))
#对多列进行（相同的）多个函数操作
functions = ['count', 'mean', 'max']
result = grouped['tip_pct', 'total_bill'].agg(functions)
print(result)
print(result['tip_pct'])
#自定义列名
ftuples = [('Durchschnitt', 'mean'), ('Abweichung', np.var)]
print(grouped['tip_pct', 'total_bill'].agg(ftuples))
#对不同列进行不同的函数操作，传入列名到函数的字典
print(grouped.agg({'tip' : np.max, 'size' : 'sum'}))
#对不同列进行不同数目的不同函数操作
print(grouped.agg({'tip_pct' : ['min', 'max', 'mean', 'std'],'size' : 'sum'}))
#transform,apply 操作
people = DataFrame(np.random.randn(5, 5),columns=['a', 'b', 'c', 'd', 'e'],index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])
def demean(arr):
    return arr - arr.mean()
key = ['one', 'two', 'one', 'two', 'one']
demeaned = people.groupby(key).transform(demean)
print(demeaned)
print(demeaned.groupby(key).mean())
#将apply中的函数用于各个分组，再进行聚合，“拆分，应用，合并”
def top(df, n=5, column='tip_pct'):
    return df.sort_index(by=column)[-n:]
top(tips, n=6)
tips.groupby('smoker').apply(top)
tips.groupby(['smoker', 'day']).apply(top, n=1, column='total_bill')
#禁用分组建索引
tips.groupby('smoker', group_keys=False).apply(top)

#利用随机序列抽样，N为抽样个数，len求样本数
#deck.take(np.random.permutation(len(deck))[:n])
#分组加权品均
df = DataFrame({'category': ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b'],
                'data': np.random.randn(8),
                'weights': np.random.rand(8)})
print(df)
grouped = df.groupby('category')
get_wavg = lambda g: np.average(g['data'], weights=g['weights'])
print(grouped.apply(get_wavg))
#分组求相关系数
close_px = pd.read_csv(r'E:\mydata\stock_px.csv', parse_dates=True, index_col=0)
close_px.info()
print(close_px[-4:])
rets = close_px.pct_change().dropna()
print(rets)
spx_corr = lambda x: x.corrwith(x['SPX'])
by_year = rets.groupby(lambda x: x.year)
print(by_year.apply(spx_corr))
# Annual correlation of Apple with Microsoft
print(by_year.apply(lambda g: g['AAPL'].corr(g['MSFT'])))
#
import statsmodels.api as sm
def regress(data, yvar, xvars):
    Y = data[yvar]
    X = data[xvars]
    X['intercept'] = 1.
    result = sm.OLS(Y, X).fit()
    return result.params
print(by_year.apply(regress, 'AAPL', ['SPX']))#前者是序列，后者加中括号
#透视表，默认函数为mean
tips.pivot_table(index=['sex', 'smoker'])
tips.pivot_table(['tip_pct', 'size'], index=['sex', 'day'],
                 columns='smoker')
#margins=True，添加分项小计
tips.pivot_table(['tip_pct', 'size'], index=['sex', 'day'],
                 columns='smoker', margins=True)
#aggfunc设置函数，这里得到分组大小也可以用count
tips.pivot_table('tip_pct', index=['sex', 'smoker'], columns='day',
                 aggfunc=len, margins=True)
#去掉NA
tips.pivot_table('size', index=['time', 'sex', 'smoker'],
                 columns='day', aggfunc='sum', fill_value=0)
#交叉表，用于计算分组频率
#建立数据
from StringIO import StringIO
data = """\
Sample    Gender    Handedness
1    Female    Right-handed
2    Male    Left-handed
3    Female    Right-handed
4    Male    Right-handed
5    Male    Left-handed
6    Male    Right-handed
7    Female    Right-handed
8    Female    Left-handed
9    Male    Right-handed
10    Female    Right-handed"""
data = pd.read_table(StringIO(data), sep='\s+')
pd.crosstab(data.Gender, data.Handedness, margins=True)
pd.crosstab([tips.time, tips.day], tips.smoker, margins=True)