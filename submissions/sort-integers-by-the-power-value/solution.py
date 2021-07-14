// https://leetcode.com/problems/sort-integers-by-the-power-value

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        ls = []
        for i in range(lo, hi+1):
            a = i
            cnt = 0
            while a != 1:
                if a % 2 == 0:
                    a = a // 2
                else:
                    a = a * 3 + 1
                cnt += 1
            ls.append([cnt, i])
        ls = sorted(ls)
        return ls[k-1][1]
