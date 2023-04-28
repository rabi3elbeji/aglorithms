def heapify(array, n, i):
    """
    The heapify function takes an array, the length of the array, and a starting index. It then compares that
    starting index to its children (left and right) to see if it is larger than either of them. If so, it swaps with
    whichever child is larger until there are no more children or until the parent node is greater than both children.

    :param array: Pass in the array that we want to heapify
    :param n: Specify the size of the heap
    :param i: Specify the index of the root node
    :return: In-place array
    :doc-author: Rabii Elbeji
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and array[left] > array[largest]:
        largest = left

    if right < n and array[right] > array[largest]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        # Call heapify recursively on the affected subtree.
        heapify(array, n, largest)


def heap_sort(array):
    """
    The heap_sort function takes an array as input and returns a sorted version of the array.
    The function uses the heapify function to build a max heap from the given array, then extracts
    the elements one by one and places them in order at the end of the list. The remaining elements are
    then re-heapified until all elements have been extracted.

    :param array: Pass in the array to be sorted
    :return: The array sorted in ascending order
    :doc-author: Rabii Elbeji
    """
    n = len(array)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        # Call heapify on the remaining heap.
        heapify(array, i, 0)

    return array


# Test the implementation with an unsorted array
array = [3, 5, 1, 4, 2]
sorted_array = heap_sort(array)
print(sorted_array)  # Output: [1, 2, 3, 4, 5]
