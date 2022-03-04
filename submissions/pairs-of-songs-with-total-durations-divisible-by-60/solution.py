from collections import Counter
from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        reminders = [t % 60 for t in time]
        counter = Counter(reminders)
        ans = 0
        for r in reminders:
            if r == 0 or r == 30:
                ans += counter[r] - 1
            else:
                ans += counter[60 - r]
            counter[r] -= 1

        return ans
