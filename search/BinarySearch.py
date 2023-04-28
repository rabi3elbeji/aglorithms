def binary_search(arr, target):
    """
    The binary_search function takes in a sorted array and a target value.
    It returns the index of the target value if it is found, otherwise - 1.

    :param arr: Pass in the array that we want to search through
    :param target: Find the index of a given value in an array
    :return: The index of the target element if it is found in the array
    :doc-author: Rabii Elbeji
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Test cases
arr1 = [2, 4, 6, 8, 10]
target1 = 6
result1 = binary_search(arr1, target1)
print(result1)  # Output: 2

arr2 = ['apple', 'banana', 'cherry', 'date']
target2 = 'banana'
result2 = binary_search(arr2, target2)
print(result2)  # Output: 1

arr3 = [10, 20, 30, 40, 50]
target3 = 60
result3 = binary_search(arr3, target3)
print(result3)  # Output: -1
