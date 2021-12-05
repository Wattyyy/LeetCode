# https://leetcode.com/problems/number-of-different-integers-in-a-string

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        str_nums = {str(i) for i in range(10)}
        word = word + 'a'
        stack = []
        new = []
        for char in word:
            if char in str_nums:
                new.append(char)
            else:
                if 0 < len(new):
                    stack.append(''.join(new))
                new = []
        ret = set()
        for item in stack:
            ret.add(int(item))
        return len(ret)
