// https://leetcode.com/problems/isomorphic-strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        used = set()
        for s_char, t_char in zip(s, t):
            if s_char not in mapping:
                if t_char not in used:
                    mapping[s_char] = t_char
                    used.add(t_char)
                else:
                    return False
            elif mapping[s_char] != t_char:
                return False
        return True
                
                
        