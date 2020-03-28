# https://leetcode.com/problems/nth-digit/

class Solution:
    # 10 ~ 189th digit -> (10, 99)
    # 190 ~ 2889th digit -> (100, 999)
    # 2900 ~ 38889th digit -> (1000, 10000)
    # ...
    def findNthDigit(self, n):
        if n < 10:
            return n
        sum_val = 9
        for i in range(2, 11):
            if n < 9 * i * 10 ** (i - 1):
                break
            sum_val += 9 * i * 10 ** (i - 1)
        diff = n - (sum_val + 1)
        num = int(diff / i) + 10 ** (i - 1)
        str_num = str(num)
        return int(str_num[diff % i])

        
