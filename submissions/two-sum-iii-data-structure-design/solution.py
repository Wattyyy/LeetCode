// https://leetcode.com/problems/two-sum-iii-data-structure-design

from collections import defaultdict
class TwoSum:

    def __init__(self):
        self.list = []
        
    def add(self, number):
        self.list.append(number)
        
    def find(self, value):
        N = len(self.list)
        target_idx = defaultdict(list)
        for i in range(N):
            target_idx[value - self.list[i]].append(i)
        for i in range(N):
            if self.list[i] in target_idx:
                indices = target_idx[self.list[i]]
                for idx in indices:
                    if idx != i:
                        return True
        return False 

        
# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)