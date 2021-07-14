// https://leetcode.com/problems/reconstruct-itinerary

from collections import defaultdict, Counter
from copy import deepcopy
import sys
sys.setrecursionlimit(10 ** 7)

class Solution:
    def findItinerary(self, tickets):
        graph = defaultdict(list)
        edge_counter = Counter()
        for f, t in tickets:
            graph[f].append(t)
            edge_counter[(f, t)] += 1
        for key in graph:
            graph[key] = sorted(graph[key])

        output = []
        def backtrack(node='JFK', current=['JFK'], i=0):
            if len(output) == 1:
                return 
            elif i == len(tickets):
                output.append(deepcopy(current))
            else:
                for nx in graph[node]:
                    if edge_counter[(node, nx)] > 0:
                        current.append(nx)
                        edge_counter[(node, nx)] -= 1
                        backtrack(nx, current, i+1)
                        current.pop()
                        edge_counter[(node, nx)] += 1

        backtrack()
        return output[0]