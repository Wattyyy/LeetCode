// https://leetcode.com/problems/generate-random-point-in-a-circle

import random
from math import sqrt

class Solution:

    def __init__(self, radius, x_center, y_center):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center
        
    def randPoint(self):
        while True:
            xr = random.uniform(-self.radius, self.radius)
            yr = random.uniform(-self.radius, self.radius)
            if sqrt(xr**2 + yr**2) > self.radius:
                continue
            else:
                x = self.x_center + xr
                y = self.y_center + yr
                return [x, y]