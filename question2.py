def remove_duplicates(sequence):
    seen = set()  # To keep track of elements we've seen
    result = []

    for item in sequence:
        if item not in seen:
            seen.add(item)  # Add the element to the set to mark it as seen
            result.append(item)

    return result

# Test case
input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]
