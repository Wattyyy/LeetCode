// https://leetcode.com/problems/count-largest-group

from collections import defaultdict
class Solution:
    def countLargestGroup(self, n: int) -> int:
        sum2group = defaultdict(list)
        max_size = 0
        for num in range(1, n+1):
            str_num = str(num)
            sum_val = 0
            for sn in str_num:
                sum_val += int(sn)
            sum2group[sum_val].append(num)
            max_size = max(max_size, len(sum2group[sum_val]))

        ans = 0
        for key in sum2group:
            if len(sum2group[key]) == max_size:
                ans += 1
        return ans

