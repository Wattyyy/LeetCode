# https://leetcode.com/problems/my-calendar-i

from bisect import bisect_left
class MyCalendar:

    def __init__(self):
        self.start = []
        self.end = []
        
    def book(self, start: int, end: int) -> bool:
        if len(self.start) == 0:
            self.start.append(start)
            self.end.append(end)
            return True
        
        idx = bisect_left(self.start, start)
        if idx == len(self.start):
            if self.end[-1] <= start:
                self.start.append(start)
                self.end.append(end)
                return True
            else:
                return False
        
        if idx == 0:
            if end <= self.start[0]:
                self.start.insert(0, start)
                self.end.insert(0, end)
                return True
            else:
                return False
        
        if self.end[idx-1] <= start and end <= self.start[idx]:
            self.start.insert(idx, start)
            self.end.insert(idx, end)
            return True
        else:
            return False




# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)