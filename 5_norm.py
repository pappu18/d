import pandas as pd
import numpy as np
df=pd.read_csv('employees.csv')

sum=(df['SALARY']**2).sum()
data_sum = df['SALARY']/np.sqrt(sum)
print(data_sum)
