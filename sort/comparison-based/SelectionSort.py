def selection_sort(array):
    """
    The selection_sort function sorts an array of integers in ascending order.

    :param array: Pass the array to be sorted into the function
    :return: The sorted array
    :doc-author: Rabii Elbeji
    """
    n = len(array)  # Get the length of the input array
    for i in range(n - 1):  # Iterate through the unsorted part of the list
        # Find the minimum element in the unsorted part of the list
        min_index = i  # Set the minimum element index to the current element
        for j in range(i + 1, n):  # Iterate through the rest of the unsorted part of the list
            if array[j] < array[min_index]:  # If the current element is smaller than the minimum element
                min_index = j  # Update the minimum element index

        # Swap the minimum element with the first element of the unsorted part of the list
        temp = array[i]  # Store the current element in a temporary variable
        array[i] = array[min_index]  # Replace the current element with the minimum element
        array[min_index] = temp  # Replace the minimum element with the current element

    return array  # Return the sorted array


# Test the implementation with an unsorted array
array = [3, 5, 1, 4, 2]
sorted_array = selection_sort(array)
print(sorted_array)  # Output: [1, 2, 3, 4, 5]
