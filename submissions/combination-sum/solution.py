# https://leetcode.com/problems/combination-sum


class Solution:
    def combinationSum(self, candidates, target):
        output = set()
        N = len(candidates)

        def backtrack(cur_sum=0, cur_list=[]):
            if cur_sum == target:
                output.add(tuple(sorted(cur_list[:])))
            if cur_sum < target:
                for i in range(N):
                    cur_list.append(candidates[i])
                    backtrack(cur_sum + candidates[i], cur_list)
                    cur_list.pop()

        backtrack()
        ans = []
        for item in output:
            ans.append(list(item))
        return ans
