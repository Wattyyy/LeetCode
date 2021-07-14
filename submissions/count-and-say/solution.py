// https://leetcode.com/problems/count-and-say

class Solution:
    def countAndSay(self, n: int):
        d = {1: '1', 2: '11'}
        for i in range(3, 31):
            ptr = 0
            string = d[i-1]
            tmp, new = [], []
            while ptr < len(string):
                tmp.append(string[ptr])
                if (ptr == len(string)-1) or (string[ptr] != string[ptr+1]):
                    new.append(str(len(tmp)) + tmp[0])
                    tmp = []
                ptr += 1
            d[i] = ''.join(new)
        return d[n]
        