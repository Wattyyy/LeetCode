// https://leetcode.com/problems/longest-string-chain

from typing import List
from collections import deque

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        graph = {word:[] for word in words}
        dist = {word:-1 for word in words}
        for word in words:
            for i in range(len(word)):
                key = word[:i] + word[i+1:]    
                if key in graph:
                    graph[word].append(key)
            
        tmp = sorted([(len(word), word) for word in words], reverse=True)
        for _, word in tmp:
            if 1<= dist[word]:
                continue
            queue = deque([(word, 1)])
            while queue:
                key, cnt = queue.pop()
                dist[key] = cnt
                for nk in graph[key]:
                    if dist[nk] < cnt + 1:
                        queue.append((nk, cnt + 1))
        return max(dist.values())
 