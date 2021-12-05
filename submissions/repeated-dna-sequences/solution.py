# https://leetcode.com/problems/repeated-dna-sequences

class Solution:
    def findRepeatedDnaSequences(self, s):
        if len(s) < 10: return []
        nucle_map = {'A':2, 'C':3, 'G':5, 'T':7}
        hash_val = 0
        for i in range(10):
            val = nucle_map[s[i]]
            hash_val += val * (10 ** i)
        hash_map = {hash_val: [1, (0, 9)]}
        for j in range(10, len(s)):
            old_val, new_val = nucle_map[s[j-10]], nucle_map[s[j]]
            hash_val = int((hash_val - old_val) / 10) + new_val * (10 ** 9)
            if hash_val not in hash_map:
                hash_map[hash_val] = [1, (j-9, j)]
            else:
                hash_map[hash_val][0] += 1
            
        ans = []
        for key, val in hash_map.items():
            if val[0] > 1:
                l, r = val[1][0], val[1][1]
                ans.append(s[l:r+1])
        return ans
        
        
            
        
        