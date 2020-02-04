# https://leetcode.com/problems/course-schedule/

from collections import defaultdict
class Solution:
    def isCyclic(self, v, visited, rec_visited): 
        visited[v] = True
        rec_visited[v] = True
        for neighbor in self.graph[v]: 
            if rec_visited[neighbor]: 
                return True
            if (not visited[neighbor]) and self.isCyclic(neighbor, visited, rec_visited):
                return True
        rec_visited[v] = False
        return False

    def canFinish(self, numCourses, prerequisites):
        if not prerequisites:
            return True
        self.graph = defaultdict(list)
        for i in range(len(prerequisites)):
            value, key = prerequisites[i]
            self.graph[key].append(value)
        visited = [False for _ in range(numCourses)]
        rec_visited = [False for _ in range(numCourses)]
        
        for node in range(numCourses):
            if (not visited[node]) and (self.isCyclic(node,visited,rec_visited)):
                return False
        return True


