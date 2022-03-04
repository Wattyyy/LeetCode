from math import lcm


class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10 ** 9 + 7
        s_int, l_int = min(a, b), max(a, b)
        if l_int % s_int == 0:
            return (s_int * n) % MOD

        left, right = 2, 40000 * (10 ** 9)
        while left <= right:
            mid = (left + right) // 2
            cnt = (mid // s_int) + (mid // l_int) - (mid // lcm(s_int, l_int))
            if cnt == n:
                return max(s_int * (mid // s_int), l_int * (mid // l_int)) % MOD

            if cnt < n:
                left = mid + 1
            else:
                right = mid - 1

        return 0
