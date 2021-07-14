// https://leetcode.com/problems/word-pattern

class Solution:
    def wordPattern(self, pattern, str):
        idx = 0
        char2int = {}
        listed_pattern = list(pattern)
        for item in listed_pattern:
            if item not in char2int:
                char2int[item] = idx
                idx += 1
        pattern_indices = []
        for item in listed_pattern:
            pattern_indices.append(char2int[item])
        
        idx = 0
        str2int = {}
        listed_str = str.split(' ')
        for item in listed_str:
            if item not in str2int:
                str2int[item] = idx
                idx += 1
        str_pattern = []
        for item in listed_str:
            str_pattern.append(str2int[item])
        
        return pattern_indices == str_pattern