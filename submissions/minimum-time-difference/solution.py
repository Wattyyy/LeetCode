# https://leetcode.com/problems/minimum-time-difference

class Solution:
    def convertTime(self, time_str):
        res = int(time_str[:2])*60 + int(time_str[3:])
        return res
        
    def findMinDifference(self, timePoints):
        times = sorted([self.convertTime(time_str) for time_str in timePoints])
        ans_list = []
        ans_list.append(times[0] + 24*60 - times[-1])
        for i in range(len(times)-1):
            ans_list.append(times[i+1] - times[i])
        return min(ans_list)
        