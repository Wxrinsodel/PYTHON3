import random
import math
import matplotlib.pyplot as plt


centers = [[1, 1], [3, 1], [2, 5]] 

print(centers)

def create_data_points(centers, num_points_per_center):
  """
  Creates a group of "data points" that tend to be closer to the given centers.
  """
  all_points = []
  for center in centers:
    for _ in range(num_points_per_center): 
      x = random.gauss(center[0], 1)  # Random x that mostly around the center's x
      y = random.gauss(center[1], 1)  # Random y that mostly around the center's y
      all_points.append([x, y])
  return all_points

num_points_per_center = 300 
data_points = create_data_points(centers, num_points_per_center)
