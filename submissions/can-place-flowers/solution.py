from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        # n == 1
        if len(flowerbed) == 1:
            return flowerbed[0] == 0

        cnt = 0
        for i, v in enumerate(flowerbed):
            if v == 1:
                continue
            if i == 0:
                if flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    cnt += 1
            elif i == len(flowerbed) - 1:
                if flowerbed[i - 1] == 0:
                    flowerbed[i] = 1
                    cnt += 1
            else:
                if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    cnt += 1

            if cnt == n:
                return True

        return False
