# https://leetcode.com/problems/find-median-from-data-stream

from sortedcontainers import SortedList


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = SortedList()

    def addNum(self, num: int) -> None:
        self.s.add(num)

    def findMedian(self) -> float:
        N = len(self.s)
        if N % 2 == 0:
            return (self.s[N // 2 - 1] + self.s[N // 2]) / 2
        else:
            return float(self.s[N // 2])


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
