# https://leetcode.com/problems/counting-bits

class Solution:
    def countBits(self, num):
        if num==0:
            return [0]
        i = 1
        while 2**i <= num:
            i += 1
        count = [0 for _ in range(2**i)]
        count[1] = 1
        i = 1
        while 2**i<=num:
            for j in range(2**i, 2**i+2**(i-1)):
                count[j] = count[j-2**(i-1)]
                count[j+2**(i-1)] = count[j] + 1
            i += 1
        return count[:num+1]