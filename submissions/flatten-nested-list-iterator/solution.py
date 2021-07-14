// https://leetcode.com/problems/flatten-nested-list-iterator

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList):
        self.list = []
        def helper(ls):
            for item in ls:
                if not item.isInteger():
                    helper(item.getList())
                else:
                    self.list.append(item.getInteger())
            return
        helper(nestedList)
        self.length = len(self.list)
        self.idx = -1
        
    def next(self):
        self.idx += 1
        return self.list[self.idx]
    
    
    def hasNext(self):
        return (0 <= self.idx + 1) and (self.idx + 1 < self.length)
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())