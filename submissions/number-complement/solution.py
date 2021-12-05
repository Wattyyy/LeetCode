# https://leetcode.com/problems/number-complement


class Solution:
    def findComplement(self, num):
        bin_list = []
        for b in bin(num)[2:]:
            if b == "0":
                bin_list.append("1")
            else:
                bin_list.append("0")
        coef = 1
        ans = 0
        for n in bin_list[::-1]:
            ans += int(n) * coef
            coef *= 2
        return ans
