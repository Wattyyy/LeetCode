# https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed

from collections import defaultdict
from random import choice


class RandomizedCollection:
    def __init__(self):
        self.val2idx = defaultdict(set)
        self.list = []

    def insert(self, val):
        res = val not in self.val2idx.keys()
        idx = len(self.list)
        self.val2idx[val].add(idx)
        self.list.append(val)
        return res

    def remove(self, val):
        if len(self.val2idx[val]) > 0:
            last_item = self.list[-1]
            rm_idx = self.val2idx[val].pop()
            self.val2idx[last_item].add(rm_idx)
            self.val2idx[last_item].remove(len(self.list) - 1)
            self.list[rm_idx] = last_item
            self.list.pop()
            return True
        else:
            return False

    def getRandom(self):
        return choice(self.list)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
