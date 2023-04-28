def radix_sort(arr):
    """
    The radix_sort function takes an array of integers and sorts them in ascending order.
    It does this by using the counting sort algorithm to sort each digit from least significant
    to most significant. The function first finds the maximum number in the array, then uses that
    number to determine how many digits are needed for sorting (i.e., if max_num = 123, then 3 digits
    are needed). Then it calls counting_sort on each digit starting with 1's place and ending with 10^n's place.

    :param arr: Pass in the array that is to be sorted
    :return: In-place sorted array
    :doc-author: Rabii Elbeji
    """
    max_num = max(arr)
    digit = 1
    while max_num // digit > 0:
        counting_sort(arr, digit)
        digit *= 10


def counting_sort(arr, digit):
    """
    The counting_sort function takes in an array and a digit, and sorts the array based on that digit.
    The function first creates two arrays: count_array, which is an array of size 10 with all values initialized to 0;
    output_array, which is an empty copy of arr. Then it loops through the inputted arr and counts how many times each
    value appears in that specific place (i.e., ones place). It then adds up all previous values to get a cumulative sum
    for each index in count_array (this will be used later). Next it loops through arr backwards so as not

    :param arr: Pass in the array to be sorted
    :param digit: Determine which digit of the number we are sorting
    :return: The sorted array
    :doc-author: Rabii Elbeji
    """
    count_array = [0] * 10
    output_array = [0] * len(arr)
    for i in range(len(arr)):
        digit_value = (arr[i] // digit) % 10
        count_array[digit_value] += 1
    for i in range(1, 10):
        count_array[i] += count_array[i - 1]
    for i in range(len(arr) - 1, -1, -1):
        digit_value = (arr[i] // digit) % 10
        output_array[count_array[digit_value] - 1] = arr[i]
        count_array[digit_value] -= 1
    for i in range(len(arr)):
        arr[i] = output_array[i]


# Test the implementation with an unsorted array
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print(arr)
