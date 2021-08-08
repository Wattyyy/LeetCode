from itertools import combinations
class Solution:
    def checkPartitioning(self, s: str) -> bool:
        N = len(s)
        is_palindrome = [[False for _ in range(N)] for __ in range(N)]
        for i in reversed(range(N)):
            for j in range(i, N):
                if i == j:
                    is_palindrome[i][j] = True
                elif j - i == 1:
                    if s[i] == s[j]:
                        is_palindrome[i][j] = True
                else:
                    if is_palindrome[i+1][j-1] and s[i] == s[j]:
                        is_palindrome[i][j] = True
        
        for i1, i2 in combinations([i for i in range(N)], 2):
            if i2 - i1 == 1:
                continue
            if is_palindrome[0][i1] and is_palindrome[i1+1][i2-1] and is_palindrome[i2][N-1]:
                return True
        
        return False


                
