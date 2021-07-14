// https://leetcode.com/problems/find-duplicate-file-in-system

from typing import List
from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for path in paths:
            ls = path.split(" ")
            directory = ls[0] 
            for item in ls[1:]:
                name, content = item.split('(')
                d[content[:-1]].append(directory + '/' + name)
        res = []
        for key in d:
            if 2 <= len(d[key]):
                res.append(d[key])
        return res



            
        