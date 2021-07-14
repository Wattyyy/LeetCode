// https://leetcode.com/problems/4sum

from collections import defaultdict

class Solution:
    def fourSum(self, nums, target):
        N = len(nums)
        d = defaultdict(list)
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                key = target - nums[i] - nums[j]
                tmp_list = [i, j]
                d[key].append(tmp_list)
        
        ans_set = set()
        for k in range(N):
            for l in range(N):
                if k == l:
                    continue
                key = nums[k] + nums[l]
                for item in d[key]:
                    tmp = [k ,l] + item
                    if len(set(tmp)) == 4:
                        set_elem = sorted([nums[idx] for idx in tmp])
                        ans_set.add(tuple(set_elem))
                        
        ans_list = [list(item) for item in ans_set]
        return ans_list
                        




        


