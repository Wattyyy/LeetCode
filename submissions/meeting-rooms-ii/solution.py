# https://leetcode.com/problems/meeting-rooms-ii


class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals or intervals == [[]]:
            return 0
        min_val, max_val = float("inf"), -float("inf")
        for s, e in intervals:
            min_val = min(min_val, s)
            max_val = max(max_val, e)
        arr = [0] * (max_val + 1)
        for s, e in intervals:
            arr[s] += 1
            arr[e] -= 1
        ans = 0
        for i in range(1, max_val + 1):
            arr[i] += arr[i - 1]
            ans = max(ans, arr[i])
        return ans
