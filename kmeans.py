from sklearn.cluster import KMeans
import numpy as np

x=np.array([[1,1],[1.5,2],[3,4],[5,7],[3.5,5],[4.5, 5],[3.5, 4.5]])

centroids=np.array([[1,1],[5,7]])

kmeans=KMeans(n_clusters=2, init=centroids, n_init=1)
kmeans.fit(x)

labels=kmeans.labels_
final=kmeans.cluster_centers_

new=np.array([[2,2],[4,6]])
predict=kmeans.predict(new)

print(final)
print(predict)


import matplotlib.pyplot as plt
plt.scatter(x[:, 0], x[:, 1], c=labels)
plt.scatter(final[:, 0], final[:, 1], marker='X', color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('K-means Clustering')
plt.show()
