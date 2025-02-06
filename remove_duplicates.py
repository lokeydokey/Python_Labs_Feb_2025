def remove_duplicates(arr):
    if not arr:  # Check if the array is empty
        return arr

    # Pointer to track the position of the last unique element
    write_index = 1

    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            arr[write_index] = arr[i]  # Move the unique element to the "write" position
            write_index += 1

    return arr[:write_index]  # Return the array up to the last unique element


# Example usage
arr = [1, 1, 2, 2, 3, 4, 4, 5]
arr = remove_duplicates(arr)
print("Array after removing duplicates:", arr)
