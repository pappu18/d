from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split

'''df=load_iris()
print(df)

x=df.data
y=df.target

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)

cl=GaussianNB()
cl.fit(x_train,y_train)

y_pred=cl.predict(x_test)

print("Accuracy score: ",round(accuracy_score(y_test,y_pred),2))

print("Confusion Matrix: ")
print(confusion_matrix(y_test,y_pred))'''


import pandas as pd

df=pd.read_csv('weather.csv')
print(df)

y=df['play']

from sklearn.preprocessing import LabelEncoder

le=LabelEncoder()

df['outlook_n']=le.fit_transform(df['outlook'])
df['temperature_n']=le.fit_transform(df['temperature'])
df['humidity_n']=le.fit_transform(df['humidity'])
df['windy_n']=le.fit_transform(df['windy'])

x=df.drop(['outlook','temperature','humidity','windy','play'],axis='columns')
print(x)

cl=GaussianNB()
cl.fit(x,y)
                                               
import warnings
warnings.simplefilter(action='ignore')
print(cl.predict([[2,0,1,0]]))

print("Confusion Matrix: ")
print(confusion_matrix(y_test,y_pred))





