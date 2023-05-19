import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
'''df=pd.read_csv('employees.csv')
print(df)
sns.boxplot(x='DEPARTMENT_ID',y='SALARY',data=df)
plt.show()'''
import matplotlib.pyplot as plt
import numpy as np

# Generate random data
np.random.seed(42)
x = np.random.rand(100)
y1 = np.random.rand(100)
y2 = np.random.rand(100)

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Plot on the first subplot
ax1.scatter(x, y1)
ax1.set_xlabel('X')
ax1.set_ylabel('Y1')
ax1.set_title('Scatter Plot 1')

# Plot on the second subplot
ax2.scatter(x, y2)
ax2.set_xlabel('X')
ax2.set_ylabel('Y2')
ax2.set_title('Scatter Plot 2')

# Adjust the spacing between subplots
plt.tight_layout()

# Display the plot
plt.show()


