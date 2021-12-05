# https://leetcode.com/problems/check-if-it-is-a-straight-line

import math


class Solution:
    def checkStraightLine(self, coordinates):
        st = set()
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        x_diff, y_diff = (x2 - x1), (y2 - y1)
        div = math.gcd(x_diff, y_diff)
        x_diff, y_diff = x_diff // div, y_diff // div
        st.add((x_diff, y_diff))
        for i in range(2, len(coordinates)):
            x2, y2 = coordinates[i]
            x_diff, y_diff = (x2 - x1), (y2 - y1)
            div = math.gcd(x_diff, y_diff)
            x_diff = x_diff // div
            y_diff = y_diff // div
            if (x_diff, y_diff) not in st and (-x_diff, -y_diff) not in st:
                return False
        return True
