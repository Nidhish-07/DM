import csv
from collections import defaultdict

# Function to calculate probabilities for each class and attribute value
def train(dataset):
    class_counts = defaultdict(int)
    attribute_counts = defaultdict(lambda: defaultdict(int))
    total_samples = 0

    for row in dataset:
        class_val = row[-1]
        class_counts[class_val] += 1
        total_samples += 1

        for i in range(len(row) - 1):
            attribute_counts[i][(row[i], class_val)] += 1

    return class_counts, attribute_counts, total_samples

# Function to predict class for a given instance
def predict(class_counts, attribute_counts, total_samples, instance):
    max_prob = float('-inf')
    predicted_class = None
    probabilities = {}

    for class_val, class_count in class_counts.items():
        prob = 1.0
        for i in range(len(instance)):
            count = attribute_counts[i][instance[i], class_val]
            prob *= (count + 1) / (class_count + len(attribute_counts[i]))

        prob *= class_count / total_samples
        probabilities[class_val] = prob

        if prob > max_prob:
            max_prob = prob
            predicted_class = class_val

    sum_probs = sum(probabilities.values())
    for class_val in probabilities:
        probabilities[class_val] /= sum_probs

    return predicted_class, probabilities


def read_csv(filename):
    dataset = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            dataset.append(row)
    return dataset

if __name__ == "__main__":
    filename = 'exp12_input2.csv'
    dataset = read_csv(filename)

    class_counts, attribute_counts, total_samples = train(dataset)

    test_instance = input("Enter attributes separated by spaces: ").strip().split()

    predicted_class, probabilities = predict(class_counts, attribute_counts, total_samples, test_instance)
    print(f"Predicted class: {predicted_class}")
    print(f"Probability for 'Yes' class: {probabilities.get('Yes', 0):.4f}")
    print(f"Probability for 'No' class: {probabilities.get('No', 0):.4f}")
