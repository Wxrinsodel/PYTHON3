import numpy as np

def kmeans(data, k, max_iter=100):
    """
    Performs k-means clustering.

    Args:
        data: A NumPy array containing the data points.
        k: The number of clusters.
        max_iter: The maximum number of iterations.

    Returns:
        A tuple containing:
            - The cluster assignments for each data point.
            - The coordinates of the cluster centroids.
    """

    # Initialize centroids randomly
    centroids = data[np.random.choice(data.shape[0], k, replace=False)]

    for _ in range(max_iter):
        # Assign each data point to the nearest centroid
        distances = np.sqrt(((data - centroids[:, np.newaxis])**2).sum(axis=2))
        labels = np.argmin(distances, axis=0)

        # Update centroids
        new_centroids = np.array([data[labels == i].mean(axis=0) for i in range(k)])

        # Check for convergence
        if np.allclose(centroids, new_centroids):
            break

        centroids = new_centroids

    return labels, centroids


data = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]])
k = 5
labels, centroids = kmeans(data, k)

print("Cluster assignments:", labels)
print("Cluster centroids:", centroids)