# https://leetcode.com/problems/jump-game-ii


class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = [float("inf")] * len(nums)
        steps[0] = 0
        for i, num in enumerate(nums):
            for idx in range(i, i + num + 1):
                if len(nums) <= idx:
                    break
                steps[idx] = min(steps[idx], steps[i] + 1)

        return steps[-1]
