# Define the file name
file_name = "estelas.txt"

# Initialize a dictionary to store the count of quartets
quartet_counts = {}

# Read the file and process each line
with open(file_name, 'r') as file:
    for line in file:
        # Remove newline characters
        cleaned_line = line.strip()

        # Split the line into quartets and count occurrences
        quartets = cleaned_line.split('-')
        for i in range(len(quartets) - 3):
            quartet = f"{quartets[i]}-{quartets[i+1]}-{quartets[i+2]}-{quartets[i+3]}"
            if len(quartet) > 7:
                quartet_counts[quartet] = quartet_counts.get(quartet, 0) + 1

# Sort the quartets by the number of occurrences
sorted_quartets = sorted(quartet_counts.items(), key=lambda x: x[1], reverse=True)

total_count = sum(count for quartet, count in sorted_quartets)

print("\nContagens de quartetos de caracteres com mais do que uma ocorrência:")

# Print the sorted result with relative percentage
for quartet, count in sorted_quartets:
    if count > 1 and len(quartet) > 10:
        percentage = (count / total_count) * 100 if total_count != 0 else 0
        print(f"Quartet: {quartet}, Count: {count}, Percentage: {percentage:.2f}%")
