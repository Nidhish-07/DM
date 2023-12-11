import csv
from collections import defaultdict
import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.preprocessing import TransactionEncoder

# Define the file path for the transaction data
input_file_path = 'exp7_input.csv'

# Create a dictionary to store transactions
transactions = defaultdict(list)

# Process the CSV file to extract transaction data
with open(input_file_path, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        # Remove empty values and format the items
        items = [item.strip() for item in row if item.strip()]
        # Skip empty rows
        if items:
            transactions[len(transactions) + 1] = items

# Display the extracted transactions
print("Extracted Transactions:")
print(transactions)

# Convert transactions into a list suitable for MLxtend
transaction_list = list(transactions.values())

# Use TransactionEncoder to transform data into Apriori-compatible format
te = TransactionEncoder()
te_ary = te.fit(transaction_list).transform(transaction_list)
transformed_df = pd.DataFrame(te_ary, columns=te.columns_)

min_support = float(input("Please provide the minimum support threshold (a value between 0 and 1): "))

# Use the Apriori algorithm to find frequent itemsets
frequent_itemsets = apriori(transformed_df, min_support=min_support, use_colnames=True)

# Convert frozensets to sets for a more readable output
frequent_itemsets['itemsets'] = frequent_itemsets['itemsets'].apply(lambda x: set(x))

print("\nFrequent Itemsets:")
print(frequent_itemsets)
output_file_path = 'exp7_output.csv'
frequent_itemsets.to_csv(output_file_path, index=False)
print(f"\nThe frequent itemsets have been saved to {output_file_path}")
