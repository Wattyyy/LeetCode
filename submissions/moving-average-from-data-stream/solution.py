# https://leetcode.com/problems/moving-average-from-data-stream

from collections import deque


class MovingAverage:
    def __init__(self, size: int):
        self.cum = 0
        self.size = size
        self.queue = deque()

    def next(self, val: int) -> float:
        if len(self.queue) == self.size:
            self.cum -= self.queue[0]
            self.queue.popleft()
            self.queue.append(val)
            self.cum += self.queue[-1]
            return self.cum / len(self.queue)
        else:
            self.queue.append(val)
            self.cum += self.queue[-1]
            return self.cum / len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
