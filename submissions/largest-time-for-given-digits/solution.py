# https://leetcode.com/problems/largest-time-for-given-digits


class Solution:
    def __init__(self):
        self.ans = [-1, "00:00"]

    def backtrack(self, remain, val, used):
        if len(remain) == 4:
            for i, d in enumerate(remain):
                if d < 4:
                    val += 10 * 60 * d
                    used.append(d)
                    del remain[i]
                    self.backtrack(remain, val, used)
                    used.pop(-1)
                    remain.insert(i, d)
                    val -= 10 * 60 * d

        elif len(remain) == 3:
            for i, d in enumerate(remain):
                if (used[-1] < 2) or (used[-1] == 2 and d < 4):
                    val += 60 * d
                    used.append(d)
                    del remain[i]
                    self.backtrack(remain, val, used)
                    used.pop(-1)
                    remain.insert(i, d)
                    val -= 60 * d

        elif len(remain) == 2:
            for i, d in enumerate(remain):
                if d < 6:
                    val += 10 * d
                    used.append(d)
                    del remain[i]
                    self.backtrack(remain, val, used)
                    used.pop(-1)
                    remain.insert(i, d)
                    val -= 10 * d

        elif len(remain) == 1:
            i = 0
            d = remain[0]
            val += d
            used.append(d)
            del remain[i]
            self.backtrack(remain, val, used)
            used.pop(-1)
            remain.insert(i, d)
            val -= d

        else:
            if self.ans[0] < val:
                self.ans[0] = val
                item = str(used[0]) + str(used[1]) + ":" + str(used[2]) + str(used[3])
                self.ans[1] = item

    def largestTimeFromDigits(self, A):
        self.backtrack(A, 0, [])
        if self.ans[0] != -1:
            return self.ans[1]
        else:
            return ""
