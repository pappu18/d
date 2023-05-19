from sklearn.naive_bayes import GuassianNB
import pandas as pd
from sklearn.preprocessing import LabelEncoder

df=pd.read_csv("weather.csv")
numerics=LabelEncoder()
inputs=df.drop('play',axis='columns')
target=df['play']

inputs['outlook_n']=numerics.fit_transform(inputs['outlook'])
inputs['temp_n']=numerics.fit_transform(inputs['temperature'])
inputs['humidity_n']=numerics.fit_transform(inputs['humidity'])
inputs['windy_n']=numerics.fit_transform(inputs['windy'])
inputs_n=inputs.drop(['outlook','temperature','humidity','windy'],axis='columns')

cf=GaussianNB()
cf.fit(inputs_n,target)

import warnings
warnings.simplefilter(action='ignore')
warnings.simplefilter(action='ignore',category=FutureWarning)

print(cf.predict([[2,2,0,1]]))
