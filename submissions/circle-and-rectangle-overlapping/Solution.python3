// https://leetcode.com/problems/circle-and-rectangle-overlapping

from math import sqrt
class Solution:
    def checkOverlap(self, radius, x_center, y_center, x1, y1, x2, y2):
        rec_center_x, rec_center_y = (x1 + x2) / 2, (y1 + y2) / 2
        max_dist = radius + sqrt( (rec_center_x - x1) ** 2 + (rec_center_y - y1) ** 2 )
        dist = sqrt( (x_center - rec_center_x) ** 2 + (y_center - rec_center_y) ** 2 )
        print(dist)
        print(max_dist)
        return (dist <= max_dist)
