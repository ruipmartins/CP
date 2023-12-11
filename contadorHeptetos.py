# Define the file name
file_name = "estelas.txt"

# Initialize a dictionary to store the count of heptets
heptet_counts = {}

# Read the file and process each line
with open(file_name, 'r') as file:
    for line in file:
        # Remove newline characters
        cleaned_line = line.strip()

        # Split the line into heptets and count occurrences
        heptets = cleaned_line.split('-')
        for i in range(len(heptets) - 6):
            heptet = f"{heptets[i]}-{heptets[i+1]}-{heptets[i+2]}-{heptets[i+3]}-{heptets[i+4]}-{heptets[i+5]}-{heptets[i+6]}"
            if len(heptet) > 13:
                heptet_counts[heptet] = heptet_counts.get(heptet, 0) + 1

# Sort the heptets by the number of occurrences
sorted_heptets = sorted(heptet_counts.items(), key=lambda x: x[1], reverse=True)

total_count = sum(count for heptet, count in sorted_heptets)

print("\nContagens de heptetos de caracteres com mais do que uma ocorrência:")

# Print the sorted result with relative percentage
for heptet, count in sorted_heptets:
    if count > 1 and len(heptet) > 13:
        percentage = (count / total_count) * 100 if total_count != 0 else 0
        print(f"Heptet: {heptet}, Count: {count}, Percentage: {percentage:.2f}%")
