// https://leetcode.com/problems/map-sum-pairs

from collections import defaultdict, deque

class TrieNode:
    def __init__(self):
        self.childrendic = defaultdict(TrieNode)
        self.val = 0

        
class MapSum:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, key, val):
        cur = self.root
        for char in key:
            if char not in cur.childrendic.keys():
                cur.childrendic[char] = TrieNode()
            cur = cur.childrendic[char]
        cur.val = val

    def sum(self, prefix):
        res = 0
        cur = self.root
        for char in prefix:
            if char not in cur.childrendic.keys():
                return 0
            cur = cur.childrendic[char]
        # bfs
        queue = deque([cur])
        while queue:
            node = queue.popleft()
            res += node.val
            if node.childrendic:
                for key in node.childrendic.keys():
                    queue.append(node.childrendic[key])
        return res
        
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)