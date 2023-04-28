def interpolation_search(arr, x):
    """
    The interpolation_search function takes in a sorted array and a value to search for.
    It returns the index of the value if it is present in the array, otherwise - 1.
    The function uses interpolation search algorithm to find an item.

    :param arr: Pass in the array to be searched
    :param x: Find the value that we are looking for in the array
    :return: The index of the element x in the array arr
    :doc-author: Rabii Elbeji
    """
    low = 0
    high = len(arr) - 1

    while low <= high and x >= arr[low] and x <= arr[high]:
        pos = low + int((x - arr[low]) * (high - low) / (arr[high] - arr[low]))

        if arr[pos] == x:
            return pos
        elif arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1

    return -1


# Test cases
arr = [10, 20, 30, 40, 50]
x = 30
result = interpolation_search(arr, x)
print(result)  # output: 2

arr = [-2, 0, 3, 7, 11, 15, 18, 22, 30]
x = 15
result = interpolation_search(arr, x)
print(result)  # output: 5

arr = [1, 2, 3, 4, 5]
x = 3
result = interpolation_search(arr, x)
print(result)  # output: 2

arr = [1, 3, 5, 7, 9]
x = 2
result = interpolation_search(arr, x)
print(result)  # output: -1
