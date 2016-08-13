import pandas as pd
from pandas import Series,DataFrame
import numpy as np
mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('E:/git_download/pydata-book/ch02/movielens/movies.dat', sep='::', header=None,names=mnames,engine='python')
print(movies[:10])
genre_iter = (set(x.split('|')) for x in movies.genres)
genres = sorted(set.union(*genre_iter))
print(genres)
#需添加的矩阵
dummies = DataFrame(np.zeros((len(movies), len(genres))), columns=genres)
for i, gen in enumerate(movies.genres):
    dummies.ix[i, gen.split('|')] = 1
movies_windic = movies.join(dummies.add_prefix('Genre_'))
print(movies_windic.head())
