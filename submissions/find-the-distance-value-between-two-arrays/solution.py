# https://leetcode.com/problems/find-the-distance-value-between-two-arrays


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        ans = 0
        for i, a1 in enumerate(arr1):
            flag = True
            for j, a2 in enumerate(arr2):
                if abs(a1 - a2) <= d:
                    flag = False
            if flag:
                ans += 1

        return ans
