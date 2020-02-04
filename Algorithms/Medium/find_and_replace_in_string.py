# https://leetcode.com/problems/find-and-replace-in-string/

class Solution:
    def is_src_valid(self, S, src, idx):
        length = len(src)
        return S[idx:idx+length] == src
        

    def findReplaceString(self, S, indexes, sources, targets):
        idx2source = {}
        for idx, src, tgt in zip(indexes, sources, targets):
            idx2source[idx] = (src, tgt)
        N = len(S)
        ans = []
        idx = 0
        while idx < N:
            if idx in idx2source.keys():
                src, tgt = idx2source[idx]
                res = self.is_src_valid(S, src, idx)
                if res:
                    ans.append(tgt)
                    idx += len(src)
                else:
                    ans.append(S[idx])
                    idx += 1
            else:
                ans.append(S[idx])
                idx += 1

        return "".join(ans)
