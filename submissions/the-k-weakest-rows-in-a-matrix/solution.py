// https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix

from collections import defaultdict
class Solution:
    def kWeakestRows(self, mat, k):
        d = defaultdict(list)
        ans = []
        R, C = len(mat), len(mat[0])
        for r in range(R):
            cnt = 0
            for c in range(C):
                if mat[r][c] == 1:
                    cnt += 1
            d[cnt].append(r)
        
        for c in range(0, C+1):
            if not d[c]:
                continue
            d[c] = sorted(d[c])
            ans.extend(d[c])

        return ans[:k]

                