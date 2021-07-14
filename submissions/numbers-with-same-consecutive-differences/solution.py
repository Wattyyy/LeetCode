// https://leetcode.com/problems/numbers-with-same-consecutive-differences

class Solution:
    def __init__(self):
        self.ans = []

    def backtrack(self, current, N, K):
        if len(current) == N:
            self.ans.append( int(''.join(current)) )
            return
        for i in range(10):
            if i == 0 and len(current) == 0 and N != 1:
                continue    
            elif len(current) == 0 or abs(int(current[-1]) - i) == K:
                current.append(str(i))
                self.backtrack(current, N, K)
                current.pop(-1)
            else:
                continue

    def numsSameConsecDiff(self, N, K):
        self.backtrack([], N, K)
        return self.ans
        
        