# https://leetcode.com/problems/multiply-strings


class Solution:
    def multiply(self, num1, num2):
        char2int = {chr(48 + i): i for i in range(10)}
        int1 = 0
        for i, char in enumerate(num1):
            num = char2int[char]
            int1 += num * (10 ** (len(num1) - 1 - i))
        int2 = 0
        for i, char in enumerate(num2):
            num = char2int[char]
            int2 += num * (10 ** (len(num2) - 1 - i))
        return str(int1 * int2)
