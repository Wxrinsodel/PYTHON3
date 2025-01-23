import random
import math
import matplotlib.pyplot as plt

def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def create_data_points(centers, num_points_per_center):
    all_points = []
    for center in centers:
        for _ in range(num_points_per_center): 
            x = random.gauss(center[0], 1)
            y = random.gauss(center[1], 1)
            all_points.append([x, y])
    return all_points

def kmeans(data_points, num_clusters, max_iterations=500):
    # Choose random initial centroids
    centroids = random.sample(data_points, num_clusters)
    
    for _ in range(max_iterations):
        # Assign points to clusters
        clusters = [[] for _ in range(num_clusters)]
        for point in data_points:
            distances = [distance(point, centroid) for centroid in centroids]
            closest_centroid_index = distances.index(min(distances))
            clusters[closest_centroid_index].append(point)
        
        # Recalculate centroids
        new_centroids = []
        for cluster in clusters:
            if cluster:
                average_x = sum(p[0] for p in cluster) / len(cluster)
                average_y = sum(p[1] for p in cluster) / len(cluster)
                new_centroids.append([average_x, average_y])
        
        # Check for convergence
        if centroids == new_centroids:
            break
        
        centroids = new_centroids
    
    return centroids, clusters


centers = [[1, 1], [3, 1], [2, 5]] 
num_points_per_center = 300
num_clusters = 3


data_points = create_data_points(centers, num_points_per_center)

# Original plotting points
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.scatter([p[0] for p in data_points], [p[1] for p in data_points], s=5)
plt.title("Original Data Points")
plt.xlabel("X-coordinate")
plt.ylabel("Y-coordinate")


centroids, clusters = kmeans(data_points, num_clusters)

# Ploting clustered data points
plt.subplot(1, 2, 2)
colors = ['red', 'green', 'blue']
for i, cluster in enumerate(clusters):
    for point in cluster:
        plt.scatter(point[0], point[1], color=colors[i], s=5)

plt.scatter([c[0] for c in centroids], [c[1] for c in centroids], 
            marker='+', color='black', s=100)
plt.title("K-means Clustering")
plt.xlabel("X-coordinate")
plt.ylabel("Y-coordinate")

plt.tight_layout()
plt.show()