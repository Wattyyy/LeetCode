# https://leetcode.com/problems/minimum-index-sum-of-two-lists

from collections import defaultdict


class Solution:
    def findRestaurant(self, list1, list2):
        andy = defaultdict(int)
        doris = defaultdict(int)
        dist = defaultdict(int)
        for i in range(len(list1)):
            andy[list1[i]] = i
        for i in range(len(list2)):
            doris[list2[i]] = i
        for name in andy.keys():
            if name in doris:
                dist[name] = andy[name] + doris[name]

        ans = []
        min_key, min_val = min(dist.items(), key=lambda x: x[1])
        ans.append(min_key)
        for name in dist.keys():
            if (name != min_key) and (dist[name] == min_val):
                ans.append(name)
        return ans
