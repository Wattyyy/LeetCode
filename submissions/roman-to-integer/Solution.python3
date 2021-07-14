// https://leetcode.com/problems/roman-to-integer

class Solution:
    def romanToInt(self, s):
        num_dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        ans = 0
        i = 0
        while i<len(s):
            if i==len(s)-1:
                ans += num_dic[s[i]]
                i += 1
            else:
                if num_dic[s[i]] < num_dic[s[i+1]]:
                    ans += num_dic[s[i+1]] - num_dic[s[i]]
                    i += 2
                else:
                    ans += num_dic[s[i]]
                    i += 1
        return ans