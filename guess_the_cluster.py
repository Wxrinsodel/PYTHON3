import numpy as np
import matplotlib.pyplot as plt

points = np.genfromtxt('points_inclass.csv', delimiter=',')

min_x, max_x = points[:, 0].min(), points[:, 0].max()
min_y, max_y = points[:, 1].min(), points[:, 1].max()


def custom_kmeans(data, k, max_iters=100):
    centroids = data[np.random.choice(data.shape[0], k, replace=False)]
    
    for _ in range(max_iters):

        # Calculate Euclidean distances between each point and all centroids
        distances = np.sqrt(((data - centroids[:, np.newaxis])**2).sum(axis=2))

        #finds the index of minimum distance for each point
        labels = np.argmin(distances, axis=0)

        #taking mean of points in each cluster to reclaculate centroids
        new_centroids = np.array([data[labels == i].mean(axis=0) for i in range(k)])
        
        if np.all(centroids == new_centroids):
            break
        centroids = new_centroids
    
    return labels, centroids


n_clusters = 4
cluster_labels, centroids = custom_kmeans(points, n_clusters)


custom_colors = ['pink', 'green', 'purple', 'blue'] 

plt.figure(figsize=(10, 6))
scatter = plt.scatter(points[:, 0], points[:, 1], c=[custom_colors[label] for label in cluster_labels], s=5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='x', s=200, linewidths=2)
plt.title(f'Points Clustered into {n_clusters} Groups')
plt.xlabel('X')
plt.ylabel('Y')

plt.tight_layout()
plt.show()


print("Area Bounds:")
print(f"X range: [{min_x}, {max_x}]")
print(f"Y range: [{min_y}, {max_y}]")

print("\nCluster Centroids:")
for i, centroid in enumerate(centroids):
    print(f"Cluster {i}: {centroid}")