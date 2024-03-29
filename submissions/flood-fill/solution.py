# https://leetcode.com/problems/flood-fill


class Solution:
    def dfs(self, image, y, x, oldColor, newColor):
        image[y][x] = newColor
        nexts = [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]
        for ny, nx in nexts:
            if (
                0 <= ny < len(image)
                and 0 <= nx < len(image[0])
                and image[ny][nx] == oldColor
            ):
                self.dfs(image, ny, nx, oldColor, newColor)

    def floodFill(self, image, sr, sc, newColor):
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image
        self.dfs(image, sr, sc, oldColor, newColor)
        return image
