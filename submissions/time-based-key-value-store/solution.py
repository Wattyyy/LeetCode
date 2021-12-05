# https://leetcode.com/problems/time-based-key-value-store

# https://leetcode.com/problems/time-based-key-value-store/

from collections import defaultdict
from bisect import bisect_right
class TimeMap:

    def __init__(self):
        self.key2value = defaultdict(list)
        self.key2time = defaultdict(list)
        

    def set(self, key, value, timestamp):
        self.key2value[key].append(value)
        self.key2time[key].append(timestamp)
        
        

    def get(self, key, timestamp):
        if key not in self.key2value:
            return ""
        else:
            idx = bisect_right(self.key2time[key], timestamp) - 1
            if idx < 0:
                return ""
            else:
                return self.key2value[key][idx]



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)