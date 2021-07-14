// https://leetcode.com/problems/design-hit-counter

from bisect import bisect_right
class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.list.append(timestamp)

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        idx = bisect_right(self.list, timestamp - 300)
        return len(self.list) - idx


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)