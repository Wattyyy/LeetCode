# https://leetcode.com/problems/logger-rate-limiter

from collections import defaultdict


class Logger:
    def __init__(self):
        self.m2t = defaultdict(int)

    def shouldPrintMessage(self, timestamp, message):
        if message not in self.m2t:
            self.m2t[message] = timestamp
            return True
        else:
            if self.m2t[message] <= timestamp - 10:
                self.m2t[message] = timestamp
                return True
            else:
                return False

            return self.m2t[message] < timestamp - 10


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
