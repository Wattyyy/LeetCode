from collections import Counter


class Solution:
    def customSortString(self, order: str, str: str) -> str:
        cnt = Counter(str)
        res = []
        for char in order:
            for _ in range(cnt[char]):
                res.append(char)
            del cnt[char]

        for i in range(26):
            char = chr(97 + i)
            for _ in range(cnt[char]):
                res.append(char)

        return "".join(res)
