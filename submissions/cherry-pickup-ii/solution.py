from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        row_len, col_len = len(grid), len(grid[0])
        dp = [
            [[-1 for _ in range(col_len)] for __ in range(col_len)]
            for ___ in range(row_len)
        ]
        dp[0][0][col_len - 1] = grid[0][0] + grid[0][col_len - 1]
        for row in range(1, row_len):
            for l in range(0, col_len):
                for r in range(l + 1, col_len):
                    prev_l_ids = [l - 1, l, l + 1]
                    prev_r_ids = [r - 1, r, r + 1]
                    for prev_l in prev_l_ids:
                        for prev_r in prev_r_ids:
                            if (
                                0 <= prev_l < col_len
                                and 0 <= prev_r < col_len
                                and prev_l < prev_r
                                and dp[row - 1][prev_l][prev_r] != -1
                            ):
                                dp[row][l][r] = max(
                                    dp[row][l][r],
                                    dp[row - 1][prev_l][prev_r]
                                    + grid[row][l]
                                    + grid[row][r],
                                )

        ans = 0
        for l in range(0, col_len):
            for r in range(l + 1, col_len):
                ans = max(ans, dp[row_len - 1][l][r])
        return ans
