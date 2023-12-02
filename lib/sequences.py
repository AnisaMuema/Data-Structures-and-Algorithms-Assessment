def remove_duplicates(sequence):
    seen = set()
    new_sequence = []

    for item in sequence:
        if item not in seen:
            new_sequence.append(item)
            seen.add(item)

    return new_sequence


# test 1
input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  

# test 2
print(remove_duplicates(["apple", "banana", "apple", "orange", "banana", "cherry"]))