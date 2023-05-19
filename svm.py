import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

# Generate some random data
np.random.seed(0)
X = np.random.randn(200, 2)
y = np.logical_xor(X[:, 0] > 0, X[:, 1] > 0)

# Create and train the SVM classifier
clf = svm.SVC(kernel='linear')
clf.fit(X, y)

# Create a meshgrid to plot the decision boundary
xx, yy = np.meshgrid(np.linspace(-3, 3, 500),
                     np.linspace(-3, 3, 500))
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Plot the data points
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)

# Plot the decision boundary and margins
plt.contour(xx, yy, Z, colors=['k', 'k', 'k'],
            linestyles=['--', '-', '--'],
            levels=[-1, 0, 1])

# Set the axis labels and title
plt.xlabel('X1')
plt.ylabel('X2')
plt.title('Support Vector Machine')

# Show the plot
plt.show()
