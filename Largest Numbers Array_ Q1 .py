def find_largest_and_second_largest(arr):
    if len(arr) < 2:
        return "Array should have at least two elements"

    first_largest = second_largest = float('-inf')

    for num in arr:
        if num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif num > second_largest and num != first_largest:
            second_largest = num

    if second_largest == float('-inf'):
        return "No second largest element found"

    return first_largest, second_largest


# Example usage
arr = [10, 20, 5, 6, 80, 30, 80]
result = find_largest_and_second_largest(arr)
print("First Largest:", result[0])
print("Second Largest:", result[1])
