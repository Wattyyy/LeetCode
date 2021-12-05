# https://leetcode.com/problems/minimum-time-visiting-all-points

class Solution:
    def minTimeToVisitAllPoints(self, points):
        cx, cy = points[0]
        ans = 0
        for point in points[1:]:
            nx, ny = point
            diag = min(abs(nx - cx), abs(ny - cy))
            ans += diag
            if nx - cx < 0 and ny - cy < 0:
                ans += max( abs(nx - (cx - diag)), abs(ny - (cy - diag)) )
            elif nx - cx < 0 and ny - cy >= 0:
                ans += max( abs(nx - (cx - diag)),  abs(ny - (cy + diag)) )
            elif nx - cx >= 0 and ny - cy < 0:
                ans += max( abs(nx - (cx + diag)), abs(ny - (cy - diag)) )
            else:
                ans += max( abs(nx - (cx + diag)), abs(ny - (cy + diag)) )
            cx, cy = nx, ny

        return ans
