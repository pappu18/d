from sklearn.naive_bayes import GaussianNB
import pandas as pd
from sklearn.preprocessing import LabelEncoder

df=pd.read_csv('buys_computer.csv')
print(df)

n=LabelEncoder()
inputs=df.drop('Buys',axis='columns')
target=df['Buys']

inputs['age_n']=n.fit_transform(inputs['Age'])
inputs['income_n']=n.fit_transform(inputs['Income'])
inputs['student_n']=n.fit_transform(inputs['Student'])
inputs['Credit_rating_n']=n.fit_transform(inputs['Credit_rating'])
inputs_n = inputs.drop(['RID','Age', 'Income', 'Student', 'Credit_rating'], axis='columns')

print(inputs_n)

classifier = GaussianNB()
classifier.fit(inputs_n, target)

import warnings
warnings.simplefilter(action='ignore')
warnings.simplefilter(action='ignore', category=FutureWarning)

print("When input X = (senior, High, No, Fair)")
print(classifier.predict([[1, 0, 0, 1]]))

print("When input X = (middle-aged , Medium, No, Excellent)")
print(classifier.predict([[0, 1, 0, 0]]))


