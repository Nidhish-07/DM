import csv
import math

filepath = "exp4_input.csv"
parent = {}
child = {}

with open(filepath, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header

    i = 0
    childName = ""
    for line in reader:
        day, level, Routine, playGame, value = line

        if i == 0:
            i += 1
            choice = int(input("Enter Child Column Number: "))
            continue

        if choice == 1:
            childName = day
        elif choice == 2:
            childName = level
        elif choice == 3:
            childName = Routine
        elif choice == 4:
            childName = value
        else:
            childName = Routine

        parent[playGame] = parent.get(playGame, 0) + 1
        child[childName] = child.get(childName, {})
        child[childName][playGame] = child[childName].get(playGame, 0) + 1

parent_entropy = -((parent.get("Yes", 0) / sum(parent.values())) * math.log2(parent.get("Yes", 0) / sum(parent.values())) +
                   (parent.get("No", 0) / sum(parent.values())) * math.log2(parent.get("No", 0) / sum(parent.values())))

child_entropy = 0
for val, counts in child.items():
    pR = counts.get("Yes", 0)
    nR = counts.get("No", 0)
    tR = pR + nR
    child_entropy += -((tR / sum(parent.values())) * ((pR / tR) * math.log2(pR / tR) + (nR / tR) * math.log2(nR / tR)))

print(f"Parent Entropy: {parent_entropy}")
print(f"Child Entropy * Their portion: {child_entropy}")
print(f"Info gain: {parent_entropy - child_entropy}")
