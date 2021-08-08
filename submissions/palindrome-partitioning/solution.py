class Solution:
    def backtrack(self, s: str, idx: int, cur: List[int]) -> None:
        if idx == len(s):
            self.ans.append(cur[:])
            return
        for i in range(idx, len(s)):
            if self.is_palindrome[idx][i]:
                cur.append(s[idx:i+1])
                self.backtrack(s, i+1, cur)
                cur.pop()
        
        
    def partition(self, s: str) -> List[List[str]]:
        self.ans = []
        n = len(s)
        self.is_palindrome = [[False for _ in range(n)] for __ in range(n)]
        for i in reversed(range(n)):
            for j in range(i, n):
                if i == j:
                    self.is_palindrome[i][j] = True
                elif j - i == 1:
                    if s[i] == s[j]:
                        self.is_palindrome[i][j] = True
                else:
                    if self.is_palindrome[i+1][j-1] and s[i] == s[j]:
                        self.is_palindrome[i][j] = True
        
        self.backtrack(s, 0, [])
        return self.ans
        
        
