// https://leetcode.com/problems/insert-delete-getrandom-o1

from random import choice
class RandomizedSet:

    def __init__(self):
        self.val2idx = {}
        self.list = []

    def insert(self, val):
        if val not in self.val2idx.keys():
            idx = len(self.list)
            self.val2idx[val] = idx
            self.list.append(val)
            return True
        else:
            return False
        

    def remove(self, val):
        if val in self.val2idx.keys():
            rm_elem_idx = self.val2idx[val]
            last_elem = self.list[-1]
            last_idx = self.val2idx[last_elem]
            # swap
            self.list[rm_elem_idx] = last_elem
            self.val2idx[last_elem] = rm_elem_idx
            self.list.pop()
            del self.val2idx[val]
            return True
        else:
            return False


    def getRandom(self):
        return choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()