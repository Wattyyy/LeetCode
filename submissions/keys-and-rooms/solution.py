# https://leetcode.com/problems/keys-and-rooms

from typing import List
from collections import defaultdict, deque


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if len(rooms) == 1:
            return True
        graph = defaultdict(list)
        for i, room in enumerate(rooms):
            for key in room:
                graph[i].append(key)
        visited = set()
        queue = deque([0])
        while queue:
            v = queue.popleft()
            visited.add(v)
            for nv in graph[v]:
                if nv not in visited:
                    queue.append(nv)

        return len(visited) == len(rooms)
