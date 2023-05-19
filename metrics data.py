import pandas as pd
from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score

data=load_iris()
x=data.data
y=data.target

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)

cl=GaussianNB()
cl.fit(x_train,y_train)

y_pred=cl.predict(x_test)

print("Accuracy Score: ",accuracy_score(y_test,y_pred))
print("Precision Score: ",precision_score(y_test,y_pred, average='weighted'))
print("Recall Score: ",recall_score(y_test,y_pred, average='weighted'))
