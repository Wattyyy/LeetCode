from bisect import bisect
from collections import Counter
from typing import List

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        cnt = Counter(arr)
        arr = sorted(arr)
        for num in arr:
            if num not in cnt:
                continue

            cnt[num] -= 1
            if cnt[num] == 0:
                del cnt[num]

            if num < 0:
                if (num % 2 == 0) and (num // 2 in cnt):
                    val = num // 2
                    cnt[val] -= 1
                    if cnt[val] == 0:
                        del cnt[val]
                else:
                    return False

            else:
                val = num * 2
                if val in cnt:
                    cnt[val] -= 1
                    if cnt[val] == 0:
                        del cnt[val]
                else:
                    return False
        
        return True
