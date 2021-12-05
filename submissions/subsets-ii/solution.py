# https://leetcode.com/problems/subsets-ii


class Solution:
    def __init__(self):
        self.ans = set()

    def backtrack(self, i, cur, nums):
        if i == len(nums):
            self.ans.add(tuple(sorted(cur)))
            return
        for idx in range(i, len(nums)):
            cur.append(nums[idx])
            self.backtrack(idx + 1, cur, nums)
            cur.pop()
            self.backtrack(idx + 1, cur, nums)

    def subsetsWithDup(self, nums):
        self.backtrack(0, [], nums)
        return self.ans
