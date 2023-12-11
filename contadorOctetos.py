# Define the file name
file_name = "estelas.txt"

# Initialize a dictionary to store the count of octets
octet_counts = {}

# Read the file and process each line
with open(file_name, 'r') as file:
    for line in file:
        # Remove newline characters
        cleaned_line = line.strip()

        # Split the line into octets and count occurrences
        octets = cleaned_line.split('-')
        for i in range(len(octets) - 7):
            octet = f"{octets[i]}-{octets[i+1]}-{octets[i+2]}-{octets[i+3]}-{octets[i+4]}-{octets[i+5]}-{octets[i+6]}-{octets[i+7]}"
            if len(octet) > 15:
                octet_counts[octet] = octet_counts.get(octet, 0) + 1

# Sort the octets by the number of occurrences
sorted_octets = sorted(octet_counts.items(), key=lambda x: x[1], reverse=True)

total_count = sum(count for octet, count in sorted_octets)

print("\nContagens de octetos de caracteres com mais do que uma ocorrência:")

# Print the sorted result with relative percentage
for octet, count in sorted_octets:
    if count > 1 and len(octet) > 15:
        percentage = (count / total_count) * 100 if total_count != 0 else 0
        print(f"Octet: {octet}, Count: {count}, Percentage: {percentage:.2f}%")
