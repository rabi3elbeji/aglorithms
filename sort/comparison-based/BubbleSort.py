def bubble_sort(arr):
    """
    The bubble_sort function takes an array of integers as input and returns a sorted version of the array.
    The function uses the bubble sort algorithm to sort the elements in ascending order.

    :param arr: Pass in the array to be sorted
    :return: A sorted array
    :doc-author: Rabii Elbeji
    """

    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        # Keep a flag to identify if any swaps were made during this iteration
        # If no swaps were made, the array is already sorted and we can exit the loop
        swap_made = False

        # Last i elements are already in place, so we only need to iterate through unsorted elements
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element, and set swap_made flag to True
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_made = True

        # If no swaps were made during this iteration, the array is already sorted and we can exit the loop
        if not swap_made:
            break

    return arr


# Test the function
arr = [3, 5, 1, 4, 2]
sorted_arr = bubble_sort(arr)
print(sorted_arr)
