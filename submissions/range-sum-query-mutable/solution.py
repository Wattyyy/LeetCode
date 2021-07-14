// https://leetcode.com/problems/range-sum-query-mutable

from typing import List
class SegSumTree:
    def __init__(self, arr: List) -> None:
        self.arr = arr
        self.tree = [0] * len(arr) * 4
        self.__build_tree(0, 0, len(self.arr) - 1)
        return
    

    def __build_tree(self, node: int, start: int, end: int) -> None:
        if start == end:
            self.tree[node] = self.arr[start]
            return

        mid = (start + end) // 2
        self.__build_tree(node * 2 + 1, start, mid)
        self.__build_tree(node * 2 + 2, mid + 1, end)
        self.tree[node] = self.tree[node * 2 + 1] + self.tree[node * 2 + 2]
        return
    

    def range_sum_query(self, node: int, start: int, end: int, l: int, r: int) -> int:
        if l <= start and end <= r:
            return self.tree[node]

        if end < l or r < start:
            return 0
        
        mid = (start + end) // 2
        val1 = self.range_sum_query(node * 2 + 1, start, mid, l, r)
        val2 = self.range_sum_query(node * 2 + 2, mid + 1, end, l, r)
        return val1 + val2


    def update(self, node: int, start: int, end: int, idx: int, value: int) -> None:
        if start == end:
            self.tree[node] = value
            self.arr[idx] = value
            return
        
        mid = (start + end) // 2
        if idx <= mid:
            self.update(node * 2 + 1, start, mid, idx, value)
        else:
            self.update(node * 2 + 2, mid + 1, end, idx, value)

        self.tree[node] = self.tree[node * 2 + 1] + self.tree[node * 2 + 2]


class NumArray:

    def __init__(self, nums: List[int]):
        self.tree = SegSumTree(nums)
        self.end = len(nums) - 1

    def update(self, index: int, val: int) -> None:
        self.tree.update(0, 0, self.end, index, val)
        return 
        
    def sumRange(self, left: int, right: int) -> int:
        return self.tree.range_sum_query(0, 0, self.end, left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)