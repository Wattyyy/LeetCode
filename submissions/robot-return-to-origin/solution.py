# https://leetcode.com/problems/robot-return-to-origin


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        y = 0
        x = 0
        for s in moves:
            if s == "U":
                y += 1
            if s == "D":
                y -= 1
            if s == "R":
                x += 1
            if s == "L":
                x -= 1
        if x == 0 and y == 0:
            return True
        else:
            return False
