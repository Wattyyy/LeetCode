# https://leetcode.com/problems/count-number-of-teams


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        N = len(rating)
        if N < 3:
            return 0
        res = 0
        for i in range(N):
            for j in range(i + 1, N):
                if rating[i] < rating[j]:
                    for k in range(j + 1, N):
                        if rating[j] < rating[k]:
                            res += 1
            for j in range(i + 1, N):
                if rating[i] > rating[j]:
                    for k in range(j + 1, N):
                        if rating[j] > rating[k]:
                            res += 1
        return res
