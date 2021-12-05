# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row


class Solution:
    def minDominoRotations(self, A, B):
        if all([a == A[0] for a in A]) or all([b == B[0] for b in B]):
            return 0
        ans = float("inf")
        for n in range(1, 7):
            for j in range(2):
                tmp = 0
                if j == 0:
                    for i, v in enumerate(A):
                        if v == n:
                            continue
                        elif B[i] == n:
                            tmp += 1
                        else:
                            tmp = float("inf")
                            break
                    ans = min(ans, tmp)

                else:
                    for i, v in enumerate(B):
                        if v == n:
                            continue
                        elif A[i] == n:
                            tmp += 1
                        else:
                            tmp = float("inf")
                            break
                    ans = min(ans, tmp)

        if ans == float("inf"):
            return -1
        else:
            return ans
