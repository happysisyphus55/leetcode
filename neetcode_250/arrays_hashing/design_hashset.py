class Solution:
    def __init__(self):
        self.data = [False] * 1_000_001

    def add(self, key):
        # add a key to the hashset
        self.data[key] = True

    def remove(self, key):
        # remove a key if already marked for deletion
        self.data[key] = False

    def contains(self, key):
        # return the status of the key
        return self.data[key]
