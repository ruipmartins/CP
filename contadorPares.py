# Define the file name
file_name = "estelas.txt"

# Initialize a dictionary to store the count of pairs
pair_counts = {}

# Read the file and process each line
with open(file_name, 'r') as file:
    for line in file:
        # Remove newline characters
        cleaned_line = line.strip()

        # Split the line into pairs and count occurrences
        pairs = cleaned_line.split('-')
        for i in range(len(pairs) - 1):
            pair = f"{pairs[i]}-{pairs[i + 1]}"
            if len(pair) > 3:
                pair_counts[pair] = pair_counts.get(pair, 0) + 1

# Sort the pairs by the number of occurrences
sorted_pairs = sorted(pair_counts.items(), key=lambda x: x[1], reverse=True)

total_count = sum(count for pair, count in sorted_pairs)

print("\nContagens de pares de caracteres com mais do que uma ocorrência:")

# Print the sorted result with relative percentage
for pair, count in sorted_pairs:
    if count > 1:
        percentage = (count / total_count) * 100 if total_count != 0 else 0
        print(f"Pair: {pair}, Count: {count}, Percentage: {percentage:.2f}%")
