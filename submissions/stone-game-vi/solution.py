# https://leetcode.com/problems/stone-game-vi

class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        alice, bob = 0, 0
        arr = [[a + b, a, b] for a, b in zip(aliceValues, bobValues)]
        arr = sorted(arr, reverse=True)
        for i, item in enumerate(arr):
            if i % 2 == 0:
                alice += item[1]
            else:
                bob += item[2]
        if alice > bob:
            return 1
        elif alice == bob:
            return 0
        else:
            return -1
            