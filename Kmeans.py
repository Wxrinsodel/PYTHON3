import random
import matplotlib.pyplot as plt
import time
import numpy as np

def create_data_points(centers, num_points_per_center):
    """
    Creates a group of "data points" that tend to be closer to the given centers.
    """
    all_points = []
    for center in centers:
        for _ in range(num_points_per_center): 
            x = random.gauss(center[0], 1)
            y = random.gauss(center[1], 1)
            all_points.append([x, y])
    return np.array(all_points)

def assign_points_to_clusters(points, centroids):
    """
    Assigns each data point to the nearest centroid.
    """
    distances = np.linalg.norm(points[:, np.newaxis] - centroids, axis=2) 
    cluster_indices = np.argmin(distances, axis=1)
    return cluster_indices

def update_centroids(points, cluster_indices, k):
    """
    Updates the position of each centroid to be the average of the points in its cluster.
    """
    new_centroids = np.zeros((k, 2))  # Initialize an array for new centroids
    for i in range(k):
        cluster_points = points[cluster_indices == i] 
        if len(cluster_points) > 0: 
            new_centroids[i] = np.mean(cluster_points, axis=0) 
    return new_centroids

def kmeans(points, k, max_iterations=500):
    """
    Performs the K-means clustering algorithm.
    """
    centroids = points[np.random.choice(len(points), k, replace=False)] 

    for _ in range(max_iterations):
        cluster_indices = assign_points_to_clusters(points, centroids)
        centroids = update_centroids(points, cluster_indices, k)

    return centroids, cluster_indices


centers = [[1, 1], [3, 1], [2, 5]] 
num_points_per_center = 300
num_clusters = 3

data_points = create_data_points(centers, num_points_per_center)

# Plot the generated data points
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.scatter(data_points[:, 0], data_points[:, 1], s=5)
plt.title("Original Data Points")
plt.xlabel("X-coordinate")
plt.ylabel("Y-coordinate")

# Time the K-means execution
start_time = time.time()
centroids, cluster_indices = kmeans(data_points, num_clusters)
end_time = time.time()
print(f"K-means execution time: {end_time - start_time:.4f} seconds")

# Plot clustered data points
plt.subplot(1, 2, 2)
colors = ['red', 'yellow', 'blue']
plt.scatter(data_points[:, 0], data_points[:, 1], c=cluster_indices, s=5) 
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', color='black', s=100)
plt.title("K-means Clustering")
plt.xlabel("X-coordinate")
plt.ylabel("Y-coordinate")

plt.tight_layout()
plt.show()