import joblib
import numpy as np
import pandas as pd
import os
import sklearn
from sklearn import metrics
import joblib
import matplotlib.pyplot as plt
import matplotlib as mpl

path = "D:/onedrive/CNPS/machine_learning/input_path"
outputpath = "D:/onedrive/CNPS/machine_learning/output_path"
path_list=os.listdir(path)
for filename in path_list:
    file=path+"/"+filename
    print(file)
    data = pd.read_excel(file)  #reading data
    name=list(data.columns.values)
    Data=np.array(data)

    forest=joblib.load("D:/onedrive/CNPS/machine_learning/best_forest.pkl")
    predict=forest.predict(Data)
    print(Data.shape)
    print(predict.shape)
    Data_new=np.c_[Data,predict]
    print(Data_new)
    new_Data=pd.DataFrame(Data_new)
    outfile=outputpath+"/"+filename
    new_Data.to_excel(outfile,index=False,header=False)
#data=np.concatenate([Data,predict],axis=1)
#print(data.shape)
