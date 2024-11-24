import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np

# Load the Iris dataset
iris = datasets.load_iris()
X = pd.DataFrame(iris.data, columns=['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width'])
y = iris.target  # True labels

# Apply KMeans Clustering
kmeans = KMeans(n_clusters=3, random_state=42).fit(X)

# Define colormap
colormap = np.array(['red', 'lime', 'blue'])

# Plot Real Clusters
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.scatter(X['Petal_Length'], X['Petal_Width'], c=colormap[y], s=40)
plt.title('Real Clusters')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')

# Plot KMeans Clustering
plt.subplot(1, 2, 2)
plt.scatter(X['Petal_Length'], X['Petal_Width'], c=colormap[kmeans.labels_], s=40)
plt.title('KMeans Clustering')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')

# plt.tight_layout()
# plt.show()
