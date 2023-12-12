import csv
import heapq


def load_distance_matrix(filename):
  """
  Loads a distance matrix from a CSV file.

  Args:
      filename: The path to the CSV file.

  Returns:
      A 2D NumPy array representing the distance matrix.
  """
  with open(filename, "r") as f:
    reader = csv.reader(f)
    matrix = [list(map(float, row)) for row in reader]
  return matrix


def single_linkage(clusters, distances):
  """
  Performs single linkage clustering on two clusters.

  Args:
      clusters: A list of lists representing the current clusters.
      distances: The distance matrix.

  Returns:
      A tuple containing the indices of the merged clusters and the distance between them.
  """
  min_distance = float("inf")
  min_indices = (None, None)
  for i, cluster_i in enumerate(clusters):
    for j, cluster_j in enumerate(clusters):
      if i != j:
        for point_i in cluster_i:
          for point_j in cluster_j:
            distance = distances[point_i][point_j]
            if distance < min_distance:
              min_distance = distance
              min_indices = (i, j)
  return min_indices, min_distance


def agglomerative_clustering(distances, n_clusters):
  """
  Performs agglomerative hierarchical clustering with single linkage.

  Args:
      distances: The distance matrix.
      n_clusters: The desired number of clusters.

  Returns:
      A list of lists representing the final clusters.
  """
  clusters = [[i] for i in range(len(distances))]
  cluster_distances = []
  while len(clusters) > n_clusters:
    min_indices, min_distance = single_linkage(clusters, distances)
    cluster_distances.append((min_indices[0], min_indices[1], min_distance))
    cluster_i, cluster_j = min_indices
    clusters[cluster_i].extend(clusters[cluster_j])
    del clusters[cluster_j]
  return clusters, cluster_distances


def save_clusters(clusters, filename):
  """
  Saves the clusters to a CSV file.

  Args:
      clusters: A list of lists representing the clusters.
      filename: The path to the output CSV file.
  """
  with open(filename, "w") as f:
    writer = csv.writer(f)
    for i, cluster in enumerate(clusters):
      writer.writerow([i] + cluster)


def main():
  # Your code to load the distance matrix CSV filename and desired number of clusters
  distance_matrix_filename = "exp11_input.csv"
  n_clusters = 5

  # Load the distance matrix
  distances = load_distance_matrix(distance_matrix_filename)

  # Perform agglomerative clustering
  clusters, cluster_distances = agglomerative_clustering(distances, n_clusters)

  # Save the clusters to output CSV files
  for i, cluster in enumerate(clusters):
    save_clusters(cluster, f"cluster_{i+1}.csv")

  # Optionally, save the cluster distances to a separate CSV file
  save_clusters(cluster_distances, "cluster_distances.csv")


if __name__ == "__main__":
  main()