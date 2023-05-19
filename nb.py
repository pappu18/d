import numpy as np
import matplotlib.pyplot as mtp
import pandas as pd

import pandas as pd

# Load the dataset
data = pd.read_csv('weather.csv')

# Extract the categorical variables
cat_vars = ['outlook', 'temperature', 'humidity', 'windy']

# One hot encode the categorical variables
encoded_data = pd.get_dummies(data[cat_vars])

# Concatenate the encoded variables with the numerical variables
final_data = pd.concat([encoded_data, data[['play']]], axis=1)

# Print the final dataset
print(final_data)

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# define the transformers for each column
transformers = [('onehot', OneHotEncoder(), ['weather']),
                ('scaler', StandardScaler(), ['temperature', 'humidity'])]

# create the column transformer
ct = ColumnTransformer(transformers=transformers)

# apply the column transformer to the data
data_transformed = ct.fit_transform(data)
print(v)
'''data=pd.read_csv('weather.csv')
print(data)
x=data.iloc[:,[0,1,2,3]].values
y=data.iloc[:,[4]].values


from sklearn.preprocessing import OneHotEncoder
encoder = OneHotEncoder()
cat_var = data.iloc[:, 3:4].values
cat_var_encoded = encoder.fit_transform(cat_var)
data_encoded = np.concatenate((data.iloc[:, :3].values, cat_var_encoded, data.iloc[:, 4:].values), axis=1)

# Split data into training and testing sets
x = data_encoded[:, :-1]
y = data_encoded[:, -1:]
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=0)

# Scale input variables using StandardScaler
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)
print(x_test)'''
