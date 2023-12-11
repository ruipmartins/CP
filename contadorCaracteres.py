def count_occurrences_from_file(file_path, separator, exclude_strings):
    # Read the content of the file
    with open(file_path, 'r') as file:
        content = file.read()

    # Split the content into a list of numbers
    numbers = content.split(separator)

    # Initialize an empty dictionary to store counts
    counts = {}

    # Count occurrences of each number (excluding spaces, newline, and specific strings)
    for number in numbers:
        stripped_number = number.strip()  # Remove leading and trailing spaces
        if stripped_number and stripped_number != "\n" and stripped_number != "" and stripped_number not in exclude_strings:
            if stripped_number in counts:
                counts[stripped_number] += 1
            else:
                counts[stripped_number] = 1

    return counts

# Example usage:
file_path = "estelas.txt"
separator = "-"  # Change this to the actual separator used in your file
exclude_strings = ["<quebra de linha>", "<separação>", "??"]  # Add strings to exclude
result = count_occurrences_from_file(file_path, separator, exclude_strings)

# Calculate the total count
total_count = sum(result.values())

# Sort the result by occurrences in descending order
sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=True)

print("\nContagem ordenada de frequência de caracteres em todas as estelas:")

# Print the sorted result with relative percentage
for number, count in sorted_result:
    percentage = (count / total_count) * 100 if total_count != 0 else 0
    print(f"{number}: {count} occurrences ({percentage:.2f}%)")
