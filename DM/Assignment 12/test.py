import csv
import math

def read_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    return data

def calculate_entropy(labels):
    # Calculate entropy
    label_counts = {}
    total_samples = len(labels)

    for label in labels:
        if label in label_counts:
            label_counts[label] += 1
        else:
            label_counts[label] = 1

    entropy = 0
    for label_count in label_counts.values():
        prob = label_count / total_samples
        entropy -= prob * math.log2(prob)

    return entropy

def calculate_info_gain(data, target_attribute):
    # Calculate Information Gain for each attribute
    total_entropy = calculate_entropy([row[-1] for row in data])
    info_gain_dict = {}

    for column in range(len(data[0])):
        if column != target_attribute:
            column_data = [row[column] for row in data]
            combined_data = list(zip(column_data, [row[-1] for row in data]))

            unique_values = set(column_data)
            weighted_entropy = 0

            for value in unique_values:
                subset = [item[1] for item in combined_data if item[0] == value]
                weight = len(subset) / len(data)
                weighted_entropy += weight * calculate_entropy(subset)

            info_gain = total_entropy - weighted_entropy
            info_gain_dict[column] = info_gain
            print(f"Information Gain for attribute at index '{column}': {info_gain}")

    return info_gain_dict

def calculate_gini_index(data, attribute):
    # Calculate Gini Index for a given attribute
    unique_values = set([row[attribute] for row in data])
    total_samples = len(data)
    gini_index = 0

    for value in unique_values:
        subset = [row[-1] for row in data if row[attribute] == value]
        proportion = len(subset) / total_samples
        gini_index += proportion * (1 - proportion)

    return gini_index

input_file_path = 'exp12_input2.csv'

data = read_csv(input_file_path)

# Assuming the last column is the target attribute
target_attribute = len(data[0]) - 1

# Calculate Information Gain for each attribute
info_gain = calculate_info_gain(data, target_attribute)

# Find the attribute with the highest Information Gain
highest_info_gain_attribute = max(info_gain, key=info_gain.get)
print(f"\nThe attribute with the highest Information Gain: {highest_info_gain_attribute}")

# Calculate Gini Index for the attribute with the highest Information Gain
gini_index_highest_info_gain = calculate_gini_index(data, highest_info_gain_attribute)
print(f"Gini Index for the attribute at index '{highest_info_gain_attribute}': {gini_index_highest_info_gain}")
    