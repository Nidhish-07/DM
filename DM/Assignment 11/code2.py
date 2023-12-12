import csv

def agglomerative_clustering(dist_matrix_file):
    # Read distance matrix from CSV file
    distance_matrix = []
    with open(dist_matrix_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            distance_matrix.append([float(val) for val in row])

    clusters = [[i] for i in range(len(distance_matrix))]  # Initialize each point as a cluster

    while len(clusters) > 1:
        # Find the indices and distance of the minimum value in the distance matrix
        min_distance = float('inf')
        min_i, min_j = -1, -1
        for i in range(len(distance_matrix)):
            for j in range(i + 1, len(distance_matrix[i])):
                if distance_matrix[i][j] < min_distance:
                    min_distance = distance_matrix[i][j]
                    min_i, min_j = i, j

        # Merge clusters based on the minimum distance
        new_cluster = clusters[min_i] + clusters[min_j]
        clusters.append(new_cluster)

        # Update distance matrix after merging clusters
        new_distances = []
        for i in range(len(distance_matrix)):
            if i != min_i and i != min_j:
                dist1 = distance_matrix[min_i][i] if i < min_i else distance_matrix[i][min_i]
                dist2 = distance_matrix[min_j][i] if i < min_j else distance_matrix[i][min_j]
                dist = min(dist1, dist2)
                new_distances.append(dist)

        # Distance to the new cluster itself (zero)
        new_distances.append(0)

        # If length mismatch occurs, return an error
        if len(distance_matrix) != len(new_distances):
            return "Error: Length mismatch between distance_matrix and new_distances"

        # Update distance matrix with merged clusters
        for i in range(len(distance_matrix)):
            if i != min_i and i != min_j:
                distance_matrix[i].append(new_distances[i])

        # Remove merged clusters from the distance matrix
        distance_matrix.pop(max(min_i, min_j))
        distance_matrix.pop(min(min_i, min_j))

        for row in distance_matrix:
            row.pop(max(min_i, min_j))
            row.pop(min(min_i, min_j))

    return clusters

def write_clusters_to_csv(clusters, output_file):
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        for cluster in clusters:
            writer.writerow(cluster)

# Example usage:
input_distance_matrix_file = 'exp11_input.csv'
output_cluster_file = 'clusters_output.csv'

final_clusters = agglomerative_clustering(input_distance_matrix_file)
if isinstance(final_clusters, list):  # Check if final_clusters is a list
    write_clusters_to_csv(final_clusters, output_cluster_file)
else:
    print(final_clusters)  # Print the error message
