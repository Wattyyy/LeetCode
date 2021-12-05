# https://leetcode.com/problems/bitwise-and-of-numbers-range

import math


class Solution:
    def count_onezero(self, n, x=None):
        if n > 0:
            p = int(math.log(n, 2))
        else:
            p = 0
        if x:
            p = int(math.log(x, 2))
        zero_count, one_count = [0] * (p + 1), [0] * (p + 1)
        for i in range(p + 1):
            div = 2 ** i
            quot = n // div
            if quot % 2 == 0:
                zero_count[i] = (quot // 2) * div + (n % div + 1)
                one_count[i] = (n + 1) - zero_count[i]
            else:
                one_count[i] = (quot // 2) * div + (n % div + 1)
                zero_count[i] = (n + 1) - one_count[i]
        return zero_count, one_count

    def rangeBitwiseAnd(self, m, n):
        ans = 0
        n_zero_count, n_one_count = self.count_onezero(n)
        if m == 0:
            for p, (num_zero, num_one) in enumerate(zip(n_zero_count, n_one_count)):
                if num_zero == 0 and 0 < num_one:
                    ans += 2 ** p

        else:
            m_zero_count, m_one_count = self.count_onezero(m - 1, n)
            for idx, (num_zero, num_one) in enumerate(zip(m_zero_count, m_one_count)):
                n_zero_count[idx] -= num_zero
                n_one_count[idx] -= num_one
            for p, (num_zero, num_one) in enumerate(zip(n_zero_count, n_one_count)):
                if num_zero == 0 and 0 < num_one:
                    ans += 2 ** p

        return ans
