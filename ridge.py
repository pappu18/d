import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.linear_model import Ridge

df=pd.read_csv('salary_data.csv')

x=df.iloc[:,:-1].values
y=df.iloc[:,-1].values

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

re=Ridge()
re.fit(x_train,y_train)

y_pred=re.predict(x_test)

print("Mean Absolute error: ",mean_absolute_error(y_pred,y_test))
print("Mean squared error: ",mean_squared_error(y_test,y_pred))
print("Root Mean squared error: ",np.sqrt(mean_squared_error(y_test,y_pred)))

import matplotlib.pyplot as plt

plt.scatter(x_train,y_train,color='orange')
plt.plot(x_train,re.predict(x_train),color='black')
plt.show()
