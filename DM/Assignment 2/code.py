import csv

# Read CSV
def read_csv(file_path):
    data = []
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            data.append(float(row[0]))
    return data

# Z-Score Normalization
def z_score_normalization(data):
    mean = sum(data) / len(data)
    std_dev = (sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5
    normalized_data = [(x - mean) / std_dev for x in data]
    return normalized_data

# Min-Max Normalization
def min_max_normalization(data, new_min, new_max):
    old_min = min(data)
    old_max = max(data)
    normalized_data = [((x - old_min) / (old_max - old_min)) * (new_max - new_min) + new_min for x in data]
    return normalized_data

# Save CSV
def write_csv(file_path, data):
    with open(file_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for val in data:
            csvwriter.writerow([val])

if __name__ == "__main__":
    file_path = './exp2_input.csv'
    data = read_csv(file_path)

    print("Select normalization type:")
    print("1. Z-Score Normalization")
    print("2. Min-Max Normalization")
    choice = int(input())

    if choice == 1:
        normalized_data = z_score_normalization(data)
    elif choice == 2:
        new_min = float(input("Enter new minimum value: "))
        new_max = float(input("Enter new maximum value: "))
        normalized_data = min_max_normalization(data, new_min, new_max)
    else:
        print("Invalid choice")
        exit(1)

    write_csv("exp2_output.csv", normalized_data)
    print("Normalization complete. Results saved to exp2_output.csv")
