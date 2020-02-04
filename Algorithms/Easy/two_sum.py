class Solution:
    def twoSum(self, nums, target):
        N = len(nums)
        dif_numidx = dict()
        for i in range(N):
            dif = target - nums[i]
            dif_numidx[dif] = [nums[i], i]

        for i in range(N):
            try:
                idx = dif_numidx[nums[i]][1]
                if idx != i: return [i, idx]
                else: continue
            except:
                continue
