import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import matplotlib as mpl
import matplotlib.patches as mpatches
import os

path = "D:/onedrive/全球CNPS循环/READS/重做/机器学习/netcdf/SPP5_8.5/ML_results"
outputpath = "D:/onedrive/全球CNPS循环/READS/重做/机器学习/netcdf/SPP5_8.5/ML_figure"

path_list=os.listdir(path)
for filename in path_list:
    file=path+"/"+filename
    data=pd.read_excel(file)

    lat = np.array(data['lat'])
    lon = np.array(data['lon'])
    pred = np.array(data['pred'])

    plt.style.use('ggplot')
    plt.figure(figsize=(10,6))

    #初始化地图对象,正常坐标
    map1 = Basemap(projection='robin', lat_0=90, lon_0=0,
            resolution='l', area_thresh=1000.0)  #初始化地图对象,正常坐标

    map1.drawcoastlines(linewidth= 0.2)      #绘制海岸线
    #map1.drawcountries(linewidth= 0.2)   #绘制国家
    map1.drawmapboundary(fill_color='white') # 海洋颜色
    map1.fillcontinents(color='lightgrey',alpha=0.5)  #填充颜色

    map1.drawmeridians(np.arange(0, 360, 60))    #绘制经线
    map1.drawparallels(np.arange(-90, 90, 30))   #绘制纬线

    cm=mpl.colors.ListedColormap(['lightgreen','blue','mediumpurple','brown','orangered','orange'])

    map1.scatter(lon, lat, latlon=True,
          alpha=1, s=3.3,c=pred,cmap=cm,linewidths=0,marker='s')

    #plt.colorbar()

    #create legend
    ET1 = mpatches.Patch(color='lightgreen', label='Type 1')
    ET2 = mpatches.Patch(color='blue', label='Type 2')
    ET3 = mpatches.Patch(color='mediumpurple', label='Type 3')
    ET4 = mpatches.Patch(color='brown', label='Type 4')
    ET5 = mpatches.Patch(color='orangered', label='Type 5')
    ET6 = mpatches.Patch(color='orange', label='Type 6')
    plt.legend(handles=[ET1,ET2,ET3,ET4,ET5,ET6], title='Ecological Status',loc=1)
    name=filename.replace('.xlsx', '')
    plt.title(name)
    outfigure = outputpath + "/" + name+".png"
    print(outfigure)
    plt.savefig(outfigure, dpi=300)
    plt.close()