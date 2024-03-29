# https://leetcode.com/problems/design-hashset


class MyHashSet:
    def __init__(self):
        self.hash_set = [False for _ in range(1000001)]

    def add(self, key):
        self.hash_set[key] = True

    def remove(self, key):
        self.hash_set[key] = False

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        """
        return self.hash_set[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
