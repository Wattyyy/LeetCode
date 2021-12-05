class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_val = values[0] - 1
        ans = 0
        for i, val in enumerate(values):
            if i == 0:
                continue
            ans = max(max_val + val, ans)
            max_val = max(max_val - 1, val - 1)

        return ans
