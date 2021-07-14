// https://leetcode.com/problems/merge-intervals

class Solution:
    def merge(self, intervals):
        N = len(intervals)
        if N==0:
            return []
        intervals = sorted(intervals)
        ans = []
        tmp_list = intervals[0]
        for i in range(1, N):
            last_end = tmp_list[1]
            start = intervals[i][0]
            cur_end = intervals[i][1]
            if start <= last_end:
                if last_end <= cur_end:
                    tmp_list[1] = cur_end
                else:
                    continue
            else:
                ans.append(tmp_list)
                tmp_list = [start, cur_end]
        ans.append(tmp_list)
        return ans