def insertion_sort(arr):
    """
    The insertion_sort function takes an array as input and sorts it in ascending order.
    It does this by iterating through the array starting from the second element,
    and inserting each element into its correct position in a sorted subarray to its left.


    :param arr: Pass in the array to be sorted
    :return: Inplace sorted array
    :doc-author: Rabii Elbeji
    """
    # iterate through the array starting from 2nd element
    # assume 1st element is already sorted
    for i in range(1, len(arr)):

        # store the current value
        value = arr[i]

        # iterate backwards through the sorted portion of the array
        # and shift elements to the right if they are greater than value
        j = i - 1
        while j >= 0 and value < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1

        # insert the value in its correct position
        arr[j + 1] = value

# Example usage:
arr = [3, 5, 1, 4, 2]
insertion_sort(arr)
print(arr)