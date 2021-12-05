# https://leetcode.com/problems/greatest-common-divisor-of-strings

class Solution:
    def make_divisors(self, n):
        divisors = []
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n//i)
        return divisors


    def gcdOfStrings(self, str1, str2):
        if len(str1) == 0 or len(str2) == 0:
            return ''
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        divisors = self.make_divisors(len(str2))
        ans = [0, '']
        for d in divisors:
            x = str2[:d]
            divisible_1 = True
            divisible_2 = True
            for idx in range(0, len(str2), d):
                if x != str2[idx:d+idx]:
                    divisible_2 = False
                if not divisible_2:
                    break
            if divisible_2:
                for idx in range(0, len(str1), d):
                    if x != str1[idx:d+idx]:
                        divisible_1 = False
                    if not divisible_1:
                        break
            if divisible_1 and divisible_2 and len(x) > ans[0]:
                ans = [len(x), x]
        
        return ans[1]


        
        