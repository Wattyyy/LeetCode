# https://leetcode.com/problems/reorder-data-in-log-files


class Solution:
    def reorderLogFiles(self, logs):
        digits = [str(i) for i in range(10)]
        l_log, d_log = [], []
        for log in logs:
            idx = log.find(" ")
            identifier, word = log[:idx], log[idx + 1 :]
            if word[0] in digits:
                d_log.append(log)
            else:
                l_log.append([identifier, word])
        l_log = sorted(l_log)
        l_log = sorted(l_log, key=lambda x: x[1])
        ans = []
        for item in l_log:
            ans.append(item[0] + " " + item[1])
        return ans + d_log
