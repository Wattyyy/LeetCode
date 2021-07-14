// https://leetcode.com/problems/first-unique-number

from collections import OrderedDict

class FirstUnique:
    def __init__(self, nums):
        self.duplicates = set()
        self.od = OrderedDict()
        for num in nums:
            if num in self.duplicates:
                continue
            elif num in self.od.keys():
                del self.od[num]
                self.duplicates.add(num)
            else:
                self.od[num] = num
        
    def showFirstUnique(self):
        if not self.od.keys():
            return -1
        else:
            res =  next(iter(self.od))
            return res        

    def add(self, value):
        if value in self.duplicates:
            return
        elif value in self.od.keys():
            del self.od[value]
            self.duplicates.add(value)
        else:
            self.od[value] = value

        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)