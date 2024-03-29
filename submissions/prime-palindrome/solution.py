# https://leetcode.com/problems/prime-palindrome


class Solution:
    def backtrack(self, i, end):
        if self.ans != float("inf"):
            return

        if i == end:
            val = int("".join(self.char_list))
            if self.check(val) and self.is_prime(val) and self.N <= val:
                self.ans = val
            return

        elif i == 0:
            for j in range(1, 10):
                self.char_list[i] = str(j)
                self.char_list[-1 - i] = str(j)
                self.backtrack(i + 1, end)
        else:
            for j in range(10):
                self.char_list[i] = str(j)
                self.char_list[-1 - i] = str(j)
                self.backtrack(i + 1, end)

    def is_prime(self, n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        # check 6k+0,2,3,4
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            # check 6k+1, 6k+5
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i = i + 6
        return True

    def check(self, val):
        # is palindrome
        str_val = str(val)
        for i in range(len(str_val) // 2):
            if str_val[i] != str_val[-1 - i]:
                return False
        return True

    def primePalindrome(self, N: int) -> int:
        self.ans = float("inf")
        self.N = N
        str_N = str(N)
        for i in range(1, 10):
            if i < len(str_N):
                continue
            self.char_list = ["0"] * i
            if i % 2 == 1:
                end = i // 2 + 1
            else:
                end = i // 2
            self.backtrack(0, end)
        return self.ans
