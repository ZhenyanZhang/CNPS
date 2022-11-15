import joblib
import numpy as np
import pandas as pd
import sklearn
from sklearn import metrics
import joblib
import matplotlib.pyplot as plt
import matplotlib as mpl

path = "D:/onedrive/CNPS/machine_learning/present.xlsx"
data = pd.read_excel(path)  #reading data
name=list(data.columns.values)
Data=np.array(data)

forest=joblib.load("D:/onedrive/CNPS/machine_learning/best_forest.pkl")
predict=forest.predict(Data)
print(Data.shape)
print(predict.shape)
Data_new=np.c_[Data,predict]
print(Data_new)
new_Data=pd.DataFrame(Data_new)
new_Data.to_excel(r'D:\onedrive\全球CNPS循环\READS\重做\功能物种多指标聚类\聚类样本分布-7type\机器学习\预测透光层\wendu_0.2_result.xlsx',index=False,header=False)
#data=np.concatenate([Data,predict],axis=1)
#print(data.shape)