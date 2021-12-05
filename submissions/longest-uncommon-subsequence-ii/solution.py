from typing import List


class Solution:
    def isSubsequence(self, src, target) -> bool:
        i = 0
        for j, _ in enumerate(target):
            if i == len(src):
                return True
            if src[i] == target[j]:
                i += 1
        return i == len(src)

    def findLUSlength(self, strs: List[str]) -> int:
        arr = sorted([(len(string), string) for string in strs], reverse=True)
        ans = -1
        for i, (len1, str1) in enumerate(arr):
            tmp = -1
            for j, (len2, str2) in enumerate(arr):
                if i == j:
                    continue
                if str1 == str2:
                    tmp = -1
                    break
                else:
                    if len2 <= len1:
                        tmp = max(tmp, len1)
                    else:
                        if self.isSubsequence(str1, str2):
                            tmp = -1
                            break
                        else:
                            tmp = max(tmp, len1)
            ans = max(ans, tmp)

        return ans
