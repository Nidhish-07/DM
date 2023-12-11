import csv
import sys
from collections import defaultdict

op = 1
fwtr = open("linkage_output.csv", "w")

def agglomerative(input_file):
    global op
    dm = defaultdict(lambda: defaultdict(int))

    with open(input_file, newline='') as file:
        reader = csv.reader(file)
        points = next(reader)[1:]  # Read point names from the first line of the input file

        for line in reader:
            point, distances = line[0], line[1:]
            for idx, dist in enumerate(distances):
                if dist:
                    dm[point][points[idx]] = int(dist)

    pt1, pt2 = '', ''
    min_dist = sys.maxsize

    # Find the two points with the minimum distance
    for p, inner_map in dm.items():
        for pp, dist in inner_map.items():
            if p != pp and dist < min_dist:
                pt1, pt2, min_dist = p, pp, dist

    print(f"Clusters Chosen: {pt1} & {pt2}")

    up, down = (pt2, pt1) if pt1 > pt2 else (pt1, pt2)
    new_pt = down + up

    # Update distances and remove old points from the matrix
    keys_to_remove = []
    for point, inner_map in dm.items():
        if point > new_pt:
            dm[point][new_pt] = min(dm[point][up], dm[point][down])

        if point == down or point == up:
            keys_to_remove.append(point)

    for point, d1 in dm[down].items():
        if point < up:
            d1 = min(d1, dm[up][point])
        else:
            d1 = min(d1, dm[point][up])

        dm[new_pt][point] = d1

    for point, mtemp in dm.items():
        if point >= up:
            d1 = dm[point][up]

            if down > point:
                d1 = min(d1, dm[down][point])
            else:
                d1 = min(d1, dm[point][down])

            dm[point][new_pt] = d1

    for key in keys_to_remove:
        del dm[key]

    # Create an output file with updated cluster data
    output = f"output{op}.csv"
    op += 1
    with open(output, 'w', newline='') as fw:
        writer = csv.writer(fw)
        writer.writerow([''] + list(dm.keys()))

        for p, inner_map in dm.items():
            writer.writerow([p] + list(inner_map.values()))

    fwtr.write(f"{down} & {up}\n")

    return output

def main():
    input_file = "linkage_input.csv"

    with open(input_file, newline='') as file1:
        reader = csv.reader(file1)
        next(reader)  # Skip header
        len_points = len(next(reader)) - 1  # Determine the number of points in the dataset

    # Repeatedly perform agglomerative clustering to create clusters
    for i in range(1, len_points - 1):
        output = agglomerative(input_file)
        input_file = output

if __name__ == "__main__":
    main()
