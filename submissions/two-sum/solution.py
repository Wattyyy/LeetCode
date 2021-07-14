// https://leetcode.com/problems/two-sum

from collections import defaultdict
class Solution:
    def twoSum(self, nums, target):
        v2i = defaultdict(list)
        for i in range(len(nums)):
            v2i[target - nums[i]].append(i)

        for i in range(len(nums)):
            if nums[i] in v2i:
                for idx in v2i[nums[i]]:
                    if idx != i:
                        return sorted([i, idx])

        