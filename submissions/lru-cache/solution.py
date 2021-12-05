# https://leetcode.com/problems/lru-cache

from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        self.od = OrderedDict()
        self.capa = capacity

    def get(self, key):
        if key not in self.od:
            return -1
        res = self.od[key]
        self.od.move_to_end(key)
        return res

    def put(self, key, value):
        if key in self.od:
            self.od[key] = value
            self.od.move_to_end(key)
            return
        if len(self.od) == self.capa:
            self.od.popitem(last=False)
            self.od[key] = value
        else:
            self.od[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
