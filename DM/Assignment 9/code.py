import csv
import numpy as np

def read_csv_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data

def extract_columns(data, col1, col2):
    header = data[0]
    col1_data = []
    col2_data = []

    col1_index = header.index(col1)
    col2_index = header.index(col2)

    for row in data[1:]:
        col1_data.append(float(row[col1_index]))
        col2_data.append(float(row[col2_index]))

    return col1_data, col2_data

def calculate_correlation_coefficient(x, y):
    n = len(x)
    mean_x = sum(x) / n
    mean_y = sum(y) / n

    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    denominator = np.sqrt(sum((x[i] - mean_x)**2 for i in range(n))) * np.sqrt(sum((y[i] - mean_y)**2 for i in range(n)))

    correlation_coefficient = numerator / denominator
    return correlation_coefficient


file_path = 'exp9_input.csv'
column_1 = 'Column1'
column_2 = 'Column2'

csv_data = read_csv_file(file_path)
col1_values, col2_values = extract_columns(csv_data, column_1, column_2)
correlation = calculate_correlation_coefficient(col1_values, col2_values)

print(f"Correlation Coefficient between {column_1} and {column_2}: {correlation}")
