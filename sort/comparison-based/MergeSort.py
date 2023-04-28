def merge_sort(array):
    """
    The merge_sort function takes an array as input and returns a sorted version of that array.
    The function uses the merge_sort algorithm to accomplish this task.

    :param array: Pass the array to be sorted into the function
    :return: A sorted array
    :doc-author: Rabii Elbeji
    """
    if len(array) <= 1:
        return array

    # Divide the input array into two halves
    middle = len(array) // 2
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])

    # Merge the two sorted halves back together using the merge function
    return merge(left, right)
def merge(left, right):
    """
    The merge function takes two sorted lists and merges them into a single sorted list.

    :param left: The left subarray
    :param right: The right subarray
    :return: A merged and sorted array
    :doc-author: Rabii Elbeji
    """
    result = [] # Initialize an empty list to hold the sorted elements
    i, j = 0, 0 # Initialize two index variables to track the position in each subarray

    # Iterate over the two subarrays in parallel and append the smallest element to the result list
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add any remaining elements from the left or right subarray to the result list
    result += left[i:]
    result += right[j:]

    # Return the sorted result list
    return result

# Test the merge sort algorithm on an unsorted array
array = [3, 5, 1, 4, 2]
sorted_array = merge_sort(array)
print(sorted_array)
