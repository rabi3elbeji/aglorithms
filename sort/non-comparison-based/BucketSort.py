def bucket_sort(arr):
    """
    The bucket_sort function takes an array of floating point numbers and sorts them in ascending order.
    The function first determines the number of buckets to use, which is equal to the length of the input array.
    It then creates a list containing that many empty lists, which will serve as our buckets. The elements from
    the input array are distributed into these buckets based on their value (i.e., 0-0.25 goes into bucket 1,
    0.26-0.5 goes into bucket 2, etc.). Each non-empty bucket is sorted using Python's builtin sort method for lists.

    :param arr: Pass in the array to be sorted
    :return: A sorted array
    :doc-author: Rabii Elbeji
    """
    num_buckets = len(arr)
    # Create a list of empty lists to serve as the buckets
    buckets = [[] for _ in range(num_buckets)]
    # Distribute the elements of the input array into the appropriate bucket
    for i in arr:
        bucket_index = int(i * num_buckets)
        buckets[bucket_index].append(i)
    # Sort each non-empty bucket
    for bucket in buckets:
        bucket.sort()
    # Concatenate the sorted elements from each bucket into the output array
    sorted_array = [item for bucket in buckets for item in bucket]
    return sorted_array


# Test the implementation with an unsorted array
arr = [0.12, 0.23, 0.01, 0.34, 0.45, 0.56, 0.67, 0.78, 0.89, 0.90]
sorted_array = bucket_sort(arr)
print(sorted_array)
