from sklearn.naive_bayes import GaussianNB

import pandas as pd
from sklearn.preprocessing import LabelEncoder

df=pd.read_csv('buys_computer.csv')
print(df)

n=LabelEncoder()

target=df['Buys']


df['Age_n']=n.fit_transform(df['Age'])
df['Income_n']=n.fit_transform(df['Income'])
df['Student_n']=n.fit_transform(df['Student'])
df['Credit_rating_n']=n.fit_transform(df['Credit_rating'])

final=df.drop(['RID','Age','Income','Student','Credit_rating','Buys'], axis='columns')
print(final)

classifier=GaussianNB()
classifier.fit(final,target)

import warnings
warnings.simplefilter(action='ignore')
warnings.simplefilter(action='ignore', category=FutureWarning )

print(classifier.predict([[1,0,0,1]]))

      

