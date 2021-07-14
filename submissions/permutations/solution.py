// https://leetcode.com/problems/permutations

class Solution:
    def permute(self, nums):
        N = len(nums)
        output = []
        def backtrack(first = 0):
            if first == N:
                output.append(nums[:])
            for i in range(first, N):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]
        backtrack()
        return output
                
        