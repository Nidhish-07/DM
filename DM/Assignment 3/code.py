import csv
import math

# equal width binning
def equal_width_binning(data, num_bins):
    min_val = min(data)
    max_val = max(data)
    bin_width = (max_val - min_val) / num_bins

    bins = []
    for i in range(num_bins):
        lower_bound = min_val + i * bin_width
        upper_bound = lower_bound + bin_width
        bin_values = [val for val in data if lower_bound <= val <= upper_bound]
        bins.append((i+1, lower_bound, upper_bound, bin_values))

    return bins

# equal frequency binning
def equal_frequency_binning(data, num_bins):
    data.sort()
    n = len(data)
    bin_size = n // num_bins
    remainder = n % num_bins

    bins = []
    start = 0
    for i in range(num_bins):
        end = start + bin_size
        if remainder > 0:
            end += 1
            remainder -= 1
        bin_values = data[start:end]
        bins.append((i+1, bin_values[0], bin_values[-1], bin_values))
        start = end

    return bins

# read_csv
def read_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        next(file)
        reader = csv.reader(file)
        for row in reader:
            data.append(float(row[0]))
    return data

# save csv
def write_csv(file_path, bins):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Bin Number", "Lower Bound", "Upper Bound", "Bin Values"])
        for bin_info in bins:
            writer.writerow(bin_info)


if __name__ == "__main__":
    file_path = "./exp3_input4.csv"
    data = read_csv(file_path)
    output_path = "./exp3_output.csv"

    print("Choose binning type:")
    print("1. Equal Width Binning")
    print("2. Equal Frequency Binning")
    choice = int(input())

    num_bins = int(input("Enter the number of bins: "))

    if choice == 1:
        bins = equal_width_binning(data, num_bins)
    elif choice == 2:
        bins = equal_frequency_binning(data, num_bins)
    else:
        print("Invalid choice")
        exit(1)

    write_csv(output_path, bins)
    print(f"Bin ranges and values saved to {output_path}")

