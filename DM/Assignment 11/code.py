import pandas as pd
from scipy.cluster.hierarchy import linkage, fcluster
import matplotlib.pyplot as plt
from io import StringIO

def read_distance_table(file_path):
    # Read the CSV distance table
    return pd.read_csv(file_path, index_col=0)

def hierarchical_clustering(distance_table):
    # Perform hierarchical clustering using single linkage
    linkage_matrix = linkage(distance_table.values, method='single', metric='euclidean')
    return linkage_matrix

def plot_dendrogram(linkage_matrix, labels):
    # Plot the dendrogram
    plt.figure(figsize=(10, 6))
    dendrogram(linkage_matrix, labels=labels, leaf_rotation=90)
    plt.title('Dendrogram')
    plt.xlabel('Data Points')
    plt.ylabel('Distance')
    plt.show()

def save_cluster_groups(linkage_matrix, labels, output_file, threshold):
    # Get cluster assignments based on a distance threshold
    clusters = fcluster(linkage_matrix, threshold, criterion='distance')

    # Create a DataFrame with cluster assignments
    cluster_df = pd.DataFrame({'Data_Point': labels, 'Cluster': clusters})

    # Save cluster assignments to a CSV file
    cluster_df.to_csv(output_file, index=False)

file_path = 'exp11_input.csv'
output_file = 'exp11_output.csv'

distance_table = read_distance_table(file_path)

# Get labels (assuming row/column names are the data point identifiers)
labels = distance_table.index.tolist()

# Perform hierarchical clustering
linkage_matrix = hierarchical_clustering(distance_table)

# Plot dendrogram
plot_dendrogram(linkage_matrix, labels)

# Set a threshold for cluster assignment
threshold = 2.0

save_cluster_groups(linkage_matrix, labels, output_file, threshold)
