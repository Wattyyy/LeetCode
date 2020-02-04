# https://leetcode.com/problems/group-anagrams/

from collections import defaultdict
class Solution: 
    def groupAnagrams(self, strs):
        ans = []
        ana_dic = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            ana_dic[key].append(word)
        for key in ana_dic.keys():
            ans.append(ana_dic[key])
        return ans
