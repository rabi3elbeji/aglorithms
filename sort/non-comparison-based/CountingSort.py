def counting_sort(arr):
    """
    The counting_sort function takes an array of integers as input and returns a sorted version of the array.
    The function uses counting sort to accomplish this task.

    :param arr: Pass the array to be sorted
    :return: The sorted array
    :doc-author: Rabii Elbeji
    """
    # Determine the maximum and minimum elements in the array
    max_element = int(max(arr))
    min_element = int(min(arr))

    # Determine the range of elements in the array
    range_of_elements = max_element - min_element + 1

    # Create a count array and initialize it to all 0's
    count_arr = [0 for _ in range(range_of_elements)]

    # Traverse the input array and increment the value in the count array at the index of the element.
    for i in range(0, len(arr)):
        count_arr[arr[i] - min_element] += 1

    # Modify the count array such that each element at each index stores the sum of previous counts.
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    # Create an output array and initialize it to all 0's
    output_arr = [0 for _ in range(len(arr))]

    # Traverse the input array from right to left, and for each element, use the value in
    # the count array at that index to determine the index of the element in the output array.
    for i in range(len(arr) - 1, -1, -1):
        output_arr[count_arr[arr[i] - min_element] - 1] = arr[i]
        count_arr[arr[i] - min_element] -= 1

    # Return the sorted array
    return output_arr

# Test the implementation with an unsorted array
array = [3, 5, 1, 4, 2]
sorted_array = counting_sort(array)
print(sorted_array)  # Output: [1, 2, 3, 4, 5]