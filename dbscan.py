from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score
from sklearn.datasets import load_iris
import pandas as pd

data=load_iris()

x=data.data

cl=DBSCAN(eps=0.6, min_samples=3)
cl.fit(x)

labels=cl.fit_predict(x)
print(labels)

print("Silhouette Score: ",silhouette_score(x,labels))

import matplotlib.pyplot as plt

plt.scatter(x[:,0],x[:,1],c=labels)
plt.show()
