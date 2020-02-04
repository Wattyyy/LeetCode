# https://leetcode.com/problems/lru-cache/

from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity):
        self.dic = OrderedDict()
        self.capacity = capacity
        
    def get(self, key):
        if key in self.dic.keys():
            self.dic.move_to_end(key)
            return self.dic[key]
        else:
            return -1
        
    def put(self, key, value):
        if key in self.dic.keys():
            self.dic[key] = value
            self.dic.move_to_end(key)
        else:
            self.dic[key] = value
        if len(self.dic) > self.capacity:
            self.dic.popitem(last=False)
        
        
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
