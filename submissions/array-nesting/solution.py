from typing import List

class Solution:
    def dfs(self, node, cnt):
        next_node = self.graph[node]
        if next_node in self.visited:
            return cnt
        else:
            self.visited.add(next_node)
            return self.dfs(next_node, cnt+1)

    def arrayNesting(self, nums: List[int]) -> int:
        self.graph = {}
        for node in nums:
            self.graph[node] = nums[node]  
        ans = 1
        self.visited = set()
        for node in nums:
            if node not in self.visited:
                self.visited.add(node)
                res = self.dfs(node, 1)
                ans = max(ans, res)

        return ans
        



