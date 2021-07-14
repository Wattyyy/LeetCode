// https://leetcode.com/problems/letter-tile-possibilities

from copy import deepcopy

class Solution:
    def __init__(self):
        self.ans_set = set()
        
    def dfs(self, str_list, tiles, visited, length):
        if len(str_list)==length:
            string = "".join(str_list)
            self.ans_set.add(string)
            return
        for i in range(len(tiles)):
            if i not in visited:
                str_list_copy = deepcopy(str_list)
                str_list_copy.append(tiles[i])
                visited_copy = deepcopy(visited)
                visited_copy.add(i)
                self.dfs(str_list_copy, tiles, visited_copy, length)
        
    def numTilePossibilities(self, tiles):
        N = len(tiles)
        str_list = []
        visited = set()
        for length in range(1, N+1):
            self.dfs(str_list, tiles, visited, length)
        return len(self.ans_set)