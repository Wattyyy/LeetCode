# https://leetcode.com/problems/fibonacci-number


class Solution:
    def fib(self, n: int) -> int:
        fib = [0] * 31
        fib[1] = 1
        for i in range(2, 31):
            fib[i] = fib[i - 1] + fib[i - 2]
        return fib[n]
