// https://leetcode.com/problems/xor-queries-of-a-subarray

# https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix_xor = [0]
        for num in arr:
            val = num ^ prefix_xor[-1]
            prefix_xor.append(val)
        ans = []
        for i, j in queries:
            val = prefix_xor[j+1] ^ prefix_xor[i]
            ans.append(val)
        return ans

        