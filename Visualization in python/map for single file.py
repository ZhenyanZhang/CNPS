import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import matplotlib as mpl
import matplotlib.patches as mpatches
import os

data=pd.read_excel("D:/onedrive/全球CNPS循环/READS/重做/机器学习/netcdf/SPP585_2015_2100.xlsx")

lat = np.array(data['lat'])
lon = np.array(data['lon'])
pred = np.array(data['ID'])

plt.style.use('ggplot')
plt.figure(figsize=(10, 6))

# 初始化地图对象,正常坐标
map1 = Basemap(projection='robin', lat_0=90, lon_0=0,
               resolution='l', area_thresh=1000.0)  # 初始化地图对象,正常坐标

map1.drawcoastlines(linewidth=0.2)  # 绘制海岸线
#map1.drawcountries(linewidth=0.2)  # 绘制国家
map1.drawmapboundary(fill_color='white')  # 海洋颜色
map1.fillcontinents(color='lightgrey', alpha=0.6)  # 填充颜色

map1.drawmeridians(np.arange(0, 360, 60))  # 绘制经线
map1.drawparallels(np.arange(-90, 90, 30))  # 绘制纬线

#GROUP
cm = mpl.colors.ListedColormap(['#F90305', '#3D3E92', '#797979'])

map1.scatter(lon, lat, latlon=True,
            alpha=1, s=3.3, c=pred, cmap=cm, linewidths=0, marker='s')

#VALUE
#map1.scatter(lon, lat, latlon=True,
   #          alpha=1, s=3.3, c=pred, cmap='Reds', linewidths=0, marker='s')
plt.colorbar()


plt.show()

#plt.savefig(outfigure, dpi=300)
#plt.close()