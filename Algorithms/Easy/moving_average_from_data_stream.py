# https://leetcode.com/problems/moving-average-from-data-stream/

class MovingAverage:

    def __init__(self, size):
        self.size = size
        self.queue = []
        
        
    def next(self, val):
        if len(self.queue) < self.size:
            self.queue.append(val)
            return sum(self.queue) / len(self.queue)
            
        else:
            self.queue.pop(0)
            self.queue.append(val)
            return sum(self.queue) / self.size

