import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('employees.csv')
print(df)
sns.boxplot(x='DEPARTMENT_ID',y='SALARY',data=df)
plt.show()
