from sklearn.preprocessing import OneHotEncoder
import pandas as pd

df=pd.read_csv("employees.csv",usecols=['FIRST_NAME'])
one=OneHotEncoder(sparse=False)
data_one=one.fit_transform(df)
print("Encoded data:\n",data_one)


