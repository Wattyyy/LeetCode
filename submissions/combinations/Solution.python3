// https://leetcode.com/problems/combinations

# https://leetcode.com/problems/combinations/
class Solution:
    def combine(self, n, k):
        output = []
        def backtrack(first=1, cur_list=[]):
            if len(cur_list) == k:
                output.append(cur_list[:])
            else:
                for i in range(first, n+1):
                    cur_list.append(i)
                    backtrack(i+1, cur_list)
                    cur_list.pop()
        
        backtrack()
        return output
        
        
        
                    
                    
        