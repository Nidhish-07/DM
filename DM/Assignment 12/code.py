import pandas as pd
import math

def read_csv(file_path):
    return pd.read_csv(file_path)

def calculate_entropy(labels):
    # Calculate entropy
    unique_labels = labels.unique()
    entropy = 0
    total_samples = len(labels)

    for label in unique_labels:
        label_count = len(labels[labels == label])
        prob = label_count / total_samples
        entropy -= prob * math.log2(prob)

    return entropy

def calculate_info_gain(data, target_attribute):
    # Calculate Information Gain for each attribute
    total_entropy = calculate_entropy(data[target_attribute])
    info_gain_dict = {}

    for column in data.columns:
        if column != target_attribute:
            weighted_entropy = 0
            unique_values = data[column].unique()
            for value in unique_values:
                subset = data[data[column] == value]
                weight = len(subset) / len(data)
                weighted_entropy += weight * calculate_entropy(subset[target_attribute])
            info_gain = total_entropy - weighted_entropy
            info_gain_dict[column] = info_gain
            print(f"Information Gain for '{column}': {info_gain}")

    return info_gain_dict

def calculate_gini_index(data, attribute):
    # Calculate Gini Index for a given attribute
    unique_values = data[attribute].unique()
    total_samples = len(data)
    gini_index = 0

    for value in unique_values:
        subset = data[data[attribute] == value]
        proportion = len(subset) / total_samples
        gini_index += proportion * (1 - proportion)

    return gini_index

input_file_path = 'exp12_input2.csv'

data = read_csv(input_file_path)

# Assuming the last column is the target attribute
target_attribute = data.columns[-1]

# Calculate Information Gain for each attribute
info_gain = calculate_info_gain(data, target_attribute)

# Find the attribute with the highest Information Gain
highest_info_gain_attribute = max(info_gain, key=info_gain.get)
print(f"\nThe attribute with the highest Information Gain: {highest_info_gain_attribute}")

# Calculate Gini Index for the attribute with the highest Information Gain
gini_index_highest_info_gain = calculate_gini_index(data, highest_info_gain_attribute)
print(f"Gini Index for the attribute '{highest_info_gain_attribute}': {gini_index_highest_info_gain}")
