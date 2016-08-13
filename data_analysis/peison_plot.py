from mpl_toolkits.basemap import Basemap
import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
df_wandian = pd.read_csv(r'E:\mydata\tianchi_peison\1.csv')
df_peisondian = pd.read_csv(r'E:\mydata\tianchi_peison\2.csv')
#lllat=30.689812; urlat=31.838978; lllon=120.878227; urlon=121.971954
print(np.max(df_peisondian[['Lng','Lat']],axis=0))
print(np.min(df_peisondian[['Lng','Lat']],axis=0))
print(np.max(df_wandian[['Lng','Lat']],axis=0))
print(np.min(df_wandian[['Lng','Lat']],axis=0))
lllat=30.689812; urlat=31.838978; lllon=120.878227; urlon=121.971954
def basic_haiti_map(ax=None, lllat=30.689812,urlat=31.838978,lllon=120.878227,urlon=121.971954):
    # create polar stereographic Basemap instance.
    m = Basemap(ax=ax, projection='stere',
                lon_0=(urlon + lllon) / 2,
                lat_0=(urlat + lllat) / 2,
                llcrnrlat=lllat, urcrnrlat=urlat,
                llcrnrlon=lllon, urcrnrlon=urlon,
                resolution='f')
    # draw coastlines, state and country boundaries, edge of map.
    m.drawcoastlines()
    m.drawstates()
    m.drawcountries()
    return m

fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(30, 25))
fig.subplots_adjust(hspace=0.05, wspace=0.05)
to_plot = ['wandian', 'peisondian']
def make_plot():
    cat_data = df_wandian
    lons, lats = cat_data.Lng, cat_data.Lat
    m = basic_haiti_map(axes, lllat=lllat, urlat=urlat,
                        lllon=lllon, urlon=urlon)
    # compute map proj coordinates.
    x, y = m(lons.values, lats.values)
    m.plot(x, y, 'r.')

    cat_data = df_peisondian
    lons, lats = cat_data.Lng, cat_data.Lat
    x1, y1 = m(lons.values, lats.values)
    m.plot(x1, y1, 'g.')
    axes.set_title('%s' % 'picture')
make_plot()
plt.savefig('E:/mydata/tianchi_peison/peison.png',dpi=200,bbox_inches='tight')
plt.show()