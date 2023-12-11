import csv
import matplotlib.pyplot as plt
# Read distance matrix from CSV
def read_distance_matrix(file_path):
    distance_matrix = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            distance_matrix.append([float(val) for val in row])
    return distance_matrix

# Function to find the two closest clusters
def find_closest_clusters(dist_matrix):
    min_dist = float('inf')
    min_i, min_j = -1, -1

    for i in range(len(dist_matrix)):
        for j in range(len(dist_matrix[i])):
            if i != j and dist_matrix[i][j] < min_dist:
                min_dist = dist_matrix[i][j]
                min_i, min_j = i, j

    return min_i, min_j, min_dist

# Update distance matrix after merging clusters
def update_distance_matrix(dist_matrix, cluster_1, cluster_2):
    new_cluster = []
    new_row = []
    
    for i in range(len(dist_matrix)):
        if i != cluster_1 and i != cluster_2:
            new_dist = min(dist_matrix[i][cluster_1], dist_matrix[i][cluster_2])
            new_row.append(new_dist)
    
    # Append the new row
    new_row.append(0.0)
    dist_matrix.append(new_row)

    for row in dist_matrix:
        if len(row) > cluster_2:
            row.pop(cluster_2)

    dist_matrix.pop(cluster_2)
    for row_idx in range(len(dist_matrix)):
        if len(dist_matrix[row_idx]) > cluster_2:
            dist_matrix[row_idx].pop(cluster_2)
    
    return dist_matrix

# Main clustering function
def single_linkage_clustering(distance_matrix):
    clusters = [[i] for i in range(len(distance_matrix))]

    while len(clusters) > 1:
        cluster_1, cluster_2, min_dist = find_closest_clusters(distance_matrix)
        
        if cluster_1 >= len(clusters) or cluster_2 >= len(clusters):
            break
        
        # Create a merged cluster
        merged_cluster = clusters[cluster_1] + clusters[cluster_2]
        
        # Remove the old clusters
        del clusters[max(cluster_1, cluster_2)]
        del clusters[min(cluster_1, cluster_2)]

        # Append the merged cluster
        clusters.append(merged_cluster)

        # Update distance matrix
        distance_matrix = update_distance_matrix(distance_matrix, cluster_1, cluster_2)

    return clusters

def display_dendrogram(distance_matrix):
    clusters = [[i] for i in range(len(distance_matrix))]

    dendrogram = []
    while len(clusters) > 1:
        cluster_1, cluster_2, min_dist = find_closest_clusters(distance_matrix)
        
        # Create a dendrogram entry
        dendrogram_entry = [clusters[cluster_1][0], clusters[cluster_2][0], min_dist, len(clusters[cluster_1]) + len(clusters[cluster_2])]
        dendrogram.append(dendrogram_entry)
        
        # Merge clusters
        clusters[cluster_1].extend(clusters[cluster_2])
        del clusters[cluster_2]

        # Update distance matrix
        distance_matrix = update_distance_matrix(distance_matrix, cluster_1, cluster_2)

    # Plotting the dendrogram
    dendrogram = sorted(dendrogram, key=lambda x: x[2], reverse=True)  # Sort by distance
    plt.figure(figsize=(10, 6))
    for entry in dendrogram:
        plt.plot([entry[0], entry[1]], [entry[2], entry[2]], 'o-', color='black')
        plt.text(entry[0], entry[2], str(entry[3]), va='top', ha='center')
        plt.text(entry[1], entry[2], str(entry[3]), va='top', ha='center')

    plt.title('Dendrogram')
    plt.xlabel('Data Points')
    plt.ylabel('Distance')
    plt.show()


if __name__ == "__main__":
    # file_path = input("Enter the path to the distance matrix CSV file: ")
    file_path = "exp11_input.csv"
    distance_matrix = read_distance_matrix(file_path)

    # Perform single linkage clustering
    final_clusters = single_linkage_clustering(distance_matrix)

    # Output intermediate clusters
    with open('intermediate_clusters.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for cluster in final_clusters:
            writer.writerow(cluster)
    display_dendrogram(distance_matrix)
