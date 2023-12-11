import csv

def median(arr):
    size = len(arr)
    if size % 2 == 1:
        return arr[size // 2]
    else:
        return (arr[size // 2 - 1] + arr[size // 2]) / 2.0

def quartile1(arr):
    n = len(arr)
    first = arr[:n // 2]
    return median(first)

def quartile3(arr):
    n = len(arr)
    if n % 2 == 0:
        last = arr[n // 2:]
    else:
        last = arr[n // 2 + 1:]
    return median(last)

arr = []

with open("exp6_input.csv", "r") as in_file:
    reader = csv.reader(in_file)
    next(reader)  # Skip the header row
    for row in reader:
        if row:  # Check if the row is not empty
            mark = int(row[0])
            arr.append(mark)

if not arr:
    print("No numeric data in the CSV file.")
else:
    arr.sort()

    with open("exp6_output.csv", "w", newline="") as out_file:
        writer = csv.writer(out_file)
        writer.writerow(["", "Value"])
        writer.writerow(["Minimum value", arr[0]])
        writer.writerow(["Quartile1 value", quartile1(arr)])
        writer.writerow(["Median value", median(arr)])
        writer.writerow(["Quartile3 value", quartile3(arr)])
        writer.writerow(["Maximum value", arr[-1]])

    print("Minimum value is", arr[0])
    print("Q1:", quartile1(arr))
    print("Median:", median(arr))
    print("Q3:", quartile3(arr))
    print("Maximum value is", arr[-1])
