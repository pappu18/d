from sklearn.preprocessing import StandardScaler
import pandas as pd
import math

df=pd.read_csv("employees.csv")
data=df[['DEPARTMENT_ID']]
print("Unscaled data:\n",data)

j=math.ceil(math.log(data.max(),10))
sc=data/10**j
print(sc)
