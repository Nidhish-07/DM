def read_transactions_from_csv(file_path):
    transactions = []
    with open(file_path, 'r') as csvfile:
        for line in csvfile:
            transaction = line.strip().split(',')
            transactions.append(set(transaction))
    return transactions

def generate_frequent_itemsets(transactions, min_support):
    item_counts = {}
    for transaction in transactions:
        for item in transaction:
            if item in item_counts:
                item_counts[item] += 1
            else:
                item_counts[item] = 1

    frequent_itemsets = []
    for item, count in item_counts.items():
        if count >= min_support:
            frequent_itemsets.append([item])

    length = 2
    while True:
        candidates = []
        for i in range(len(frequent_itemsets) - 1):
            for j in range(i + 1, len(frequent_itemsets)):
                candidate = list(set(frequent_itemsets[i]) | set(frequent_itemsets[j]))
                if len(candidate) == length:
                    candidates.append(candidate)

        if not candidates:
            break

        frequent_candidates = []
        for candidate in candidates:
            support = sum(1 for transaction in transactions if set(candidate).issubset(transaction))
            if support >= min_support:
                frequent_itemsets.append(candidate)
                frequent_candidates.append(candidate)

        if not frequent_candidates:
            break

        length += 1

    return frequent_itemsets

if __name__ == "__main__":
    file_path = input("Enter the path to the CSV file: ")

    # Read transactions from CSV file
    transactions = read_transactions_from_csv(file_path)

    # Get minimum support from the user
    min_support = int(input("Enter the minimum support (e.g., 2): "))

    # Generate frequent itemsets
    frequent_itemsets = generate_frequent_itemsets(transactions, min_support)

    # Display the result
    print("\nFrequent Itemsets:")
    for itemset in frequent_itemsets:
        print(itemset)
