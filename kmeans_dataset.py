from sklearn.datasets import load_iris
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data=load_iris()
x=data.data

sc=StandardScaler()
x_new=sc.fit_transform(x)

kmeans=KMeans(n_clusters=3,n_init=10,random_state=42)
kmeans.fit(x_new)

labels=kmeans.predict(x_new)
print(labels)

#centroids
centroids=kmeans.cluster_centers_
print(centroids)

print('Score: ',silhouette_score(x_new,labels))
import matplotlib.pyplot as plt

plt.scatter(x_new[:,0],x_new[:,1],c=labels)
plt.scatter(centroids[:, 0], centroids[:, 1], marker='X', color='red')
plt.show()
