// https://leetcode.com/problems/find-the-town-judge

from collections import defaultdict
class Solution:
    def findJudge(self, N, trust):
        graph = defaultdict(set)
        for a, b in trust:
            graph[a].add(b)     
        judges = []
        for j in range(1, N + 1):
            if len(graph[j]) == 0:
                judges.append(j)
        for j in judges:
            cnt = 0
            for key in graph:
                if key == j:
                    continue
                if j in graph[key]:
                    cnt += 1
            if cnt == N - 1:
                return j
        return -1
                    

            
        
        