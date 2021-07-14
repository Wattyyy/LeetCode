// https://leetcode.com/problems/count-sorted-vowel-strings

from collections import Counter
class Solution:
    def countVowelStrings(self, n: int) -> int:
        keys = ['a', 'e', 'i', 'o', 'u']
        counter = Counter({key: 1 for key in keys})
        for i in range(2, n+1):
            new = Counter({key: 0 for key in keys})
            new['a'] += counter['a']
            new['e'] += counter['a'] + counter['e']
            new['i'] += counter['a'] + counter['e'] + counter['i']
            new['o'] += counter['a'] + counter['e'] + counter['i'] + counter['o']
            new['u'] += counter['a'] + counter['e'] + counter['i'] + counter['o'] + counter['u']
            counter = new
        
        ret = 0
        for v in counter.values():
            ret += v
        return ret
            
            

