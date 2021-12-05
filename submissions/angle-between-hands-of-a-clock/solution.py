# https://leetcode.com/problems/angle-between-hands-of-a-clock

from math import *


class Solution:
    def angleClock(self, hour, minutes):
        h_rad = ((2 * pi) * (hour + (minutes / 60))) / 12
        m_rad = (2 * pi * minutes) / 60
        h_vec = [cos(h_rad), sin(h_rad)]
        m_vec = [cos(m_rad), sin(m_rad)]
        angle = acos(
            ((h_vec[0] * m_vec[0] + h_vec[1] * m_vec[1]))
            / (
                sqrt(pow(h_vec[0], 2) + pow(h_vec[1], 2))
                * sqrt(pow(m_vec[0], 2) + pow(m_vec[1], 2))
            )
        )
        return angle * 180 / pi
