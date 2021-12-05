# https://leetcode.com/problems/robot-bounded-in-circle

from collections import deque


class Solution:
    def isRobotBounded(self, instructions):
        ls_inst = list(instructions)
        last_dir = deque([])

        end = len(ls_inst)
        for i in reversed(range(len(ls_inst))):
            char = ls_inst[i]
            if char == "G":
                break
            else:
                last_dir.appendleft(char)
                end = i

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        d = 0
        x, y = 0, 0
        for i, char in enumerate(instructions):
            if i == end:
                break
            if char == "R":
                d -= 1
                d = d % 4
            elif char == "L":
                d += 1
                d = d % 4
            else:
                x += directions[d][0]
                y += directions[d][1]

        for char in last_dir:
            if char == "R":
                d -= 1
                d = d % 4
            elif char == "L":
                d += 1
                d = d % 4

        if d != 0:
            return True
        elif d == 0 and x == y == 0:
            return True
        else:
            return False
