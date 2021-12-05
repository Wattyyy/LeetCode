# https://leetcode.com/problems/group-anagrams

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        d = defaultdict(list)
        for string in strs:
            anagram = ''.join(sorted(string))
            d[anagram].append(string)
        ans = []
        for k, v in d.items():
            ans.append(v)
        return ans