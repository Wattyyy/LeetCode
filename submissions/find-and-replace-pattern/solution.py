# https://leetcode.com/problems/find-and-replace-pattern

from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        for word in words:
            d = {}
            used_dst = set()
            flag = True
            for src, dst in zip(word, pattern):
                if src not in d.keys():
                    if dst not in used_dst:
                        d[src] = dst
                        used_dst.add(dst)
                    else:
                        flag = False
                        break
                else:
                    if d[src] != dst:
                        flag = False
                        break

            if flag:
                res.append(word)
        return res
