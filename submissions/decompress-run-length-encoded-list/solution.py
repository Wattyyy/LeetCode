# https://leetcode.com/problems/decompress-run-length-encoded-list

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ret = []
        N = len(nums)
        for i in range(0, N, 2):
            for _ in range(nums[i]):
                ret.append(nums[i+1])
        return ret
        