import numpy as np
import pandas as pd
import sys
import joblib
from sklearn.metrics import accuracy_score
from sklearn import metrics
import matplotlib as mpl
import matplotlib.pyplot as plt
import time
from sklearn.preprocessing import label_binarize
# Set properties to prevent Chinese garbled characters
mpl.rcParams['font.sans-serif'] = [u'SimHei']
mpl.rcParams['axes.unicode_minus'] = False

#file path
path="D:/onedrive/CNPS/machine_learning/ecological_types_classification.xlsx"
#k-fold cross-validation
k=10
#feature number
feature_num=31
n_classes=7
#reading data
data=pd.read_excel(path)
#path for best model
save_path="D:/onedrive/CNPS/machine_learning/best_forest.pkl"
Data=pd.read_excel(path)
Data=np.array(Data)
np.random.shuffle(Data)
num_val_sample=len(Data)//k
score_list=[]
best_score=0
#paths for saving ROC and importance figure
AUC_path="ROC.tif"
Importance_path="Importance.tif"
#input the best model
model=joblib.load(save_path)
#calculating
x_test=Data[:,0:feature_num]
y_test=Data[:,feature_num:]
y_score=model.predict_proba(x_test)
fpr=dict()
tpr=dict()
roc_auc=dict()
threshold=dict()
binarize_y_test=label_binarize(y_test,classes=[1,2,3,4,5,6,7])
for i in range(7):
    fpr[i], tpr[i], threshold[i] = metrics.roc_curve(binarize_y_test[:,i], y_score[:,i])
    roc_auc[i] = metrics.auc(fpr[i], tpr[i])

fpr['micro'], tpr['micro'], threshold['micro'] = metrics.roc_curve(binarize_y_test.ravel(), y_score.ravel())
roc_auc['micro'] = metrics.auc(fpr['micro'], tpr['micro'])

#ROC
plt.figure(1)
plt.title('Validation ROC')
plt.plot(fpr['micro'], tpr['micro'],  label = 'Average AUC = %0.2f' % roc_auc['micro'])
for i in range(7):
    plt.plot(fpr[i], tpr[i], label='%d%%'%(i*10)+' risk AUC = %0.2f' % roc_auc[i])
plt.legend(loc = 'lower right')
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.savefig(AUC_path,dpi=600)
plt.show()
#Importance
importance=model.feature_importances_
feature=['F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12',
         'F13','F14','F15','F16','F17','F18','F19','F20','F21','F22',
         'F23','F24','F25','F26','F27','F28','F29','F30','F31']  #the name of each feature were abbreviated
plt.figure(2)
plt.bar(feature,importance,width=0.4,align='center',alpha=0.8,color='#008B45FF')
for a,b in zip(feature,importance):
    plt.text(a,b+0.001,'%0.3f'%b,ha='center',va='bottom',fontsize=10)  #a,means x  b means the location of the y
plt.ylabel('Importance')
plt.xticks(feature)
plt.savefig(Importance_path,dpi=600)
plt.show()