# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        digits = digits.replace("1", "")
        N = len(digits)
        output = []
        d2c = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
              }
        
        def backtrack(first=0, cur_str=[]):
            if len(cur_str) == N:
                output.append("".join(cur_str))
            else:
                d = digits[first]
                for char in d2c[d]:
                    cur_str.append(char)
                    backtrack(first+1, cur_str)
                    cur_str.pop()
        
        backtrack()
        return output
