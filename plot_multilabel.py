import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import pickle

## Reading data
data=pd.read_csv("Dataset/data1.csv")

## Spliting into eature and target variable
X=np.array(data.loc[:,'Available MBytes':'KBytes Total'])
y=np.array(data.loc[:,'HighCPU':'NoNetwork'])

## Coverting target binary value to integer
y_val=[]
for i in range(len(y)):
    y_val.append(int(str(y[i][0])+str(y[i][1])+str(y[i][2]),2))

## Training Classifier
clf = DecisionTreeClassifier(random_state=0,max_depth=3)
clf=clf.fit(X,y_val)

## Respective Class_names
class_names=["Normal",
            "NoNetwork",
            "HighRAM",
            "HighRAM_NoNetwork",
            "HighCPU",
            "HighCPU_NoNetwork",
            "HighCPU_HighRAM",
            "HighCPU_HighRAM_NoNetwork"]

out_prev="Normal"
pred=clf.predict(X[:,:])
for i in range(pred.size):
    result=pred[i]
    if result not in [0,4]:
        out=class_names[int(result)]
        print(out)
        if out_prev != out:
            print("mqtt")
            out_prev=out
            
result=clf.predict([[390,45,0]])
print(class_names[int(result)])

"""
file_name="Classifier_model"
with open(file_name,"wb") as file:
    pickle.dump(clf,file)
"""
