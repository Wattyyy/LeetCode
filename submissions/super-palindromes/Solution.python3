// https://leetcode.com/problems/super-palindromes

class Solution:
    def __init__(self):
        self.cand = []

    def backtrack(self, i, end):
        if i == end:
            val = int(''.join(self.char_list))
            if self.check(val):
                self.ans += 1
            return
        elif i == 0:
            for j in range(1, 10):
                self.char_list[i] = str(j)
                self.char_list[-1-i] = str(j)
                self.backtrack(i+1, end)
        else:
            for j in range(10):
                self.char_list[i] = str(j)
                self.char_list[-1-i] = str(j)
                self.backtrack(i+1, end)
            

    def check(self, val):
        # is in range
        sq = pow(val, 2)
        if (sq < self.left) or (self.right < sq):
            return False

        # is palindrome
        str_sq = str(sq)
        for i in range( len(str_sq) // 2 ):
            if str_sq[i] != str_sq[-1-i]:
                return False
        return True
        
        
    def superpalindromesInRange(self, left: str, right: str) -> int:
        self.ans = 0
        self.left = int(left)
        self.right = int(right)
        for i in range(1, 10):
            self.char_list = ['0'] * i
            if i % 2 == 1:
                end = i // 2 + 1
            else:
                end = i // 2
            self.backtrack(0, end)
        return self.ans
   