# https://leetcode.com/problems/verifying-an-alien-dictionary


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        encoder = {}
        for i, char in enumerate(order):
            encoder[char] = str(i + 10)
        encoded = [["0" for _ in range(200)] for __ in range(len(words))]
        for i, word in enumerate(words):
            for j, char in enumerate(word):
                num0, num1 = encoder[char][0], encoder[char][1]
                encoded[i][2 * j] = num0
                encoded[i][2 * j + 1] = num1

        encoded = [int("".join(item)) for item in encoded]

        for num1, num2 in zip(encoded, sorted(encoded)):
            if num1 != num2:
                return False
        return True
