def linear_search(arr, target):
    """
    The linear_search function takes in an array and a target value.
    It then iterates through the array, checking if each element is equal to the target.
    If it finds a match, it returns that index. If not, it returns - 1.

    :param arr: Pass in the array that is being searched
    :param target: Find the index of the target value in an array
    :return: The index of the target element if it is present in the array
    :doc-author: Rabii Elbeji
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Test cases
arr1 = [1, 2, 3, 4, 5]
target1 = 4
result1 = linear_search(arr1, target1)
print(result1)

arr2 = ['apple', 'banana', 'cherry', 'date']
target2 = 'banana'
result2 = linear_search(arr2, target2)
print(result2)

arr3 = [10, 20, 30, 40, 50]
target3 = 60
result3 = linear_search(arr3, target3)
print(result3)
