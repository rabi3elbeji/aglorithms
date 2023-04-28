class HashTable:
    def __init__(self):
        """
        The __init__ function initializes the hash table with a size of 10.
        It also creates an empty list for each index in the hash table.

        :param self: Represent the instance of the class
        :return: A hash table of size 10
        :doc-author: Rabii Elbeji
        """
        self.size = 10
        self.hash_table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        """
        The hash_function function takes in a key and returns the index of that key within the hash table.
        The function uses modulo to determine where to place each item.

        :param self: Represent the instance of the class
        :param key: Determine the index of the hash table where an item will be stored
        :return: The remainder of the key divided by the size
        :doc-author: Rabii Elbeji
        """
        return key % self.size

    def insert(self, key, value):
        """
        The insert function takes in a key and value, then hashes the key to find the index of the bucket it belongs in.
        It then checks if that bucket already contains an item with that key. If so, it replaces its value with the new one.
        If not, it appends a tuple containing both items to that bucket.

        :param self: Refer to the object that is calling the method
        :param key: Create the hash_key
        :param value: Store the value of the key
        :return: None
        :doc-author: Rabii Elbeji
        """
        hash_key = self.hash_function(key)
        bucket = self.hash_table[hash_key]
        found = False
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (k, value)
                found = True
                break
        if not found:
            bucket.append((key, value))

    def search(self, key):
        """
        The search function takes a key as an argument and returns the value associated with that key.
        If no value is found, it returns None.

        :param self: Represent the instance of the class
        :param key: Find the hash key
        :return: The value of the key that is passed in
        :doc-author: Rabii Elbeji
        """
        hash_key = self.hash_function(key)
        bucket = self.hash_table[hash_key]
        for k, v in bucket:
            if k == key:
                return v
        return None


ht = HashTable()

ht.insert(5, "apple")
ht.insert(20, "banana")
ht.insert(10, "orange")
ht.insert(15, "peach")

assert ht.search(10) == "orange"
assert ht.search(5) == "apple"
assert ht.search(15) == "peach"

assert ht.search(30) is None
