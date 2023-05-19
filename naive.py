from sklearn.naive_bayes import GaussianNB
import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('weather.csv')
Numerics = LabelEncoder()
inputs = df.drop('play', axis='columns')
target = df['play']

inputs['outlook_n'] = Numerics.fit_transform(inputs['outlook'])
inputs['temp_n'] = Numerics.fit_transform(inputs['temperature'])
inputs['humidity_n'] = Numerics.fit_transform(inputs['humidity'])
inputs['windy_n'] = Numerics.fit_transform(inputs['windy'])
inputs_n = inputs.drop(['outlook', 'temperature', 'humidity', 'windy'], axis='columns')

print(inputs_n)

classifier = GaussianNB()
classifier.fit(inputs_n, target)

import warnings
warnings.simplefilter(action='ignore')
warnings.simplefilter(action='ignore', category=FutureWarning)

print("When input X = ( Sunny, Mild, High, True)")
print(classifier.predict([[2, 2, 0, 1]]))

print("When input X = (Overcast, cool, High, False)")
print(classifier.predict([[0, 0, 0, 0]]))

