def quick_sort(arr):
    """
    The quick_sort function takes an array of integers as input and returns a sorted version of the array.
    The quick_sort function uses the Quick Sort algorithm to sort the input array in ascending order.

    :param arr: Pass the input array to the function
    :return: A sorted array
    :doc-author: Rabii Elbeji
    """
    if len(arr) <= 1:
        return arr
    else:
        # Select the pivot element as the first element of the input array
        pivot = arr[0]
        left = []
        right = []
        # Partition the input array into two sub-arrays based on whether the element is less than or greater than the
        # pivot
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        # Recursively sort the left and right sub-arrays and combine them with the pivot to produce the final sorted
        # array
        return quick_sort(left) + [pivot] + quick_sort(right)

# Test the implementation on an unsorted array
unsorted_array = [3, 5, 1, 4, 2]
sorted_array = quick_sort(unsorted_array)
print(sorted_array)
