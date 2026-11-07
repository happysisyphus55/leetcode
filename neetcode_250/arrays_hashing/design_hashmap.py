class MyHashMap:
    def __init__(self):
        # init array with -1 to indicate empty slots
        self.data = [-1] * 1_000_001

    def put(self, key: int, value: int) -> None:
        # insert or update key-value pair in the hashmap
        self.data[key] = value

    def get(self, key: int) -> int:
        # retrieve the value associated with the given key
        return self.data[key]

    def remove(self, key: int) -> None:
        # remove the key-value pair from the hashmap
        # mark it as -1 to map it to remove
        self.data[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
