def selection_sort(arr):
    """
    Sorts a list using the Selection Sort algorithm.

    Args:
        arr (list): The list of comparable items to be sorted.

    Returns:
        list: The sorted list.
    """
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # Swap the found minimum element with the first element of the unsorted part (arr[i])
        # This places the smallest element in its correct position.
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
    return arr

# --- Example Usage ---
data = [64, 25, 12, 22, 11]
print(f"Original list: {data}")

sorted_data = selection_sort(data)
print(f"Sorted list: {sorted_data}")

# Another example
data_two = [5, 4, 3, 2, 1]
selection_sort(data_two)
print(f"Another sorted list: {data_two}")
