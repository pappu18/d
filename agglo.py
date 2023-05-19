from sklearn.cluster import AgglomerativeClustering
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.metrics import silhouette_score

data=load_iris()

x=data.data

cl=AgglomerativeClustering(n_clusters=3)
cl.fit(x)

labels=cl.labels_
print(labels)
labels=cl.fit_predict(x)
print(labels)
print("Silhoutee Score:",silhouette_score(x,labels))
import matplotlib.pyplot as plt
plt.scatter(x[:,0],x[:,1],c=labels)
plt.show()

