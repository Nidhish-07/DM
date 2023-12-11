import csv
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

v = []
with open('./exp10_input.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        _, x, y = row
        v.append((int(x), int(y)))

n = len(v)

# Calculate mid point
x_sum = sum(x for x, y in v)
y_sum = sum(y for x, y in v)
mid_x = x_sum / n
mid_y = y_sum / n
print(f"Mid Point: ({mid_x}, {mid_y})")

with open('./exp10_output.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(["", "p1", "p2", "p3", "p4", "C"])

    # Write distance matrix
    for i in range(n):
        writer.writerow(["p" + str(i + 1)] + [distance(v[i][0], v[i][1], v[j][0], v[j][1]) if i != j else 0 for j in range(n)])

    # Write nearest point and distances
    writer.writerow(["C"] + [distance(mid_x, mid_y, x, y) for x, y in v] + [0])

    # Write new center and distances
    writer.writerow([""] + ["p" + str(i + 1) for i in range(n)])
    for i in range(n):
        writer.writerow(["p" + str(i + 1)] + [distance(v[i][0], v[i][1], v[j][0], v[j][1]) if i != j else 0 for j in range(n)])

    nearest_point = min(range(n), key=lambda i: distance(mid_x, mid_y, v[i][0], v[i][1]))
    new_center_distances = [distance(v[nearest_point][0], v[nearest_point][1], x, y) for x, y in v]
    writer.writerow([f"p{nearest_point + 1} (New Center)"] + new_center_distances + [0])

print("\nDistance of each point from the center:")
for i, (x, y) in enumerate(v):
    d = distance(mid_x, mid_y, x, y)
    print(f"Distance of p{i + 1} from centre: {d}")

print("\nNearer Distance:", min(new_center_distances))
print("\nNearest point from Centre is:", f"p{nearest_point + 1}")
print("\nDistance of each point from the new center:")
for i, (x, y) in enumerate(v):
    d = distance(v[nearest_point][0], v[nearest_point][1], x, y)
    print(f"Distance of p{i + 1} from p{nearest_point + 1}: {d}")
