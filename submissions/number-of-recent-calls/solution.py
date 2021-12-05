# https://leetcode.com/problems/number-of-recent-calls

from bisect import bisect_left, bisect_right
class RecentCounter:
    def __init__(self):
        self.record = []
        
    def ping(self, t):
        self.record.append(t)
        l_idx, r_idx = bisect_left(self.record, t-3000), bisect_right(self.record, t)
        return r_idx - l_idx


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)