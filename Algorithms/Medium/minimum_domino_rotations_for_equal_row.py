# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

class Solution:
    def minDominoRotations(self, A, B):
        N = len(A)
        INF = float('inf')
        ans = INF
        for i in range(2):
            for j in range(1, 7):
                tmp = 0
                for k in range(N):
                    # make values of A equal
                    if i == 0:
                        if A[k] == j:
                            continue
                        elif B[k] == j:
                            tmp += 1
                        else:
                            tmp = INF
                            break
                    # make values of B equal
                    if i == 1:
                        if B[k] == j:
                            continue
                        elif A[k] == j:
                            tmp += 1
                        else:
                            tmp = INF
                            break
                ans = min(ans, tmp)

        if ans == INF:
            return -1
        return ans

                        


