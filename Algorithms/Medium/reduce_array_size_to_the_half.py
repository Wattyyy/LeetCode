from collections import defaultdict

class Solution:
    def minSetSize(self, arr):
        d = defaultdict(int)
        N = len(arr)
        for num in arr:
            d[num] += 1
        tuples_list = sorted(d.items(), key=lambda x: x[1], reverse=True)
        length = N
        half = N // 2
        idx = 0
        ans = 0
        while length > half:
            length -= tuples_list[idx][1]
            idx += 1
            ans += 1
        return ans
            
            

            

