# https://leetcode.com/problems/determine-color-of-a-chessboard-square


class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        char, num = coordinates[0], int(coordinates[1])
        evens = {"b", "d", "f", "h"}
        if num % 2 == 0:
            if char in evens:
                return False
            else:
                return True
        else:
            if char in evens:
                return True
            else:
                return False
