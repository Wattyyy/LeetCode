class Solution:
    def trap(self, height: List[int]) -> int:
        if sum(height) == 0:
            return 0
        water = [0] * len(height)
        for i, h in enumerate(height):
            if 0 < h:
                l_height, l_idx, st = h, i, i
                break

        for i, h in enumerate(height):
            if i <= st:
                continue
            if h < l_height:
                water[i] = l_height - h
            else:
                l_height, l_idx = h, i

        r_height, r_idx = height[len(height) - 1], len(height) - 1
        for i in reversed(range(l_idx + 1, len(height))):
            if height[i] < r_height:
                water[i] = r_height - height[i]
            else:
                r_height, r_idx = height[i], i
                water[i] = 0

        return sum(water)
