// https://leetcode.com/problems/count-primes

class Solution:
    def countPrimes(self, n: int) -> int:
        arr = [True] * (n + 1)
        for num in range(n + 1):
            if num == 0 or num == 1:
                arr[num] = False
            if arr[num]:
                i = 2
                while num * i < n + 1:
                    arr[num * i] = False
                    i += 1

        res = 0
        for i in range(n):
            if arr[i]:
                res += 1
        return res
