# https://leetcode.com/problems/design-hashset/

class MyHashSet:
    def __init__(self):
        self.bytearray = bytearray(1000001)

    def add(self, key):
        if not self.bytearray[key]:
            self.bytearray[key] = True

    def remove(self, key):
        if self.bytearray[key]:
            self.bytearray[key] = False
        

    def contains(self, key):
        if self.bytearray[key]:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
