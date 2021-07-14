// https://leetcode.com/problems/letter-combinations-of-a-phone-number

class Solution:
    def __init__(self):
        self.res = []
        self.mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'], 
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

    def backtrack(self, idx, digits, cur):
        if idx == len(digits):
            self.res.append(''.join(cur))
            return
        else:
            d = digits[idx]
            for char in self.mapping[d]:
                cur.append(char)
                self.backtrack(idx+1, digits, cur)
                cur.pop(-1)
            return
        

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return self.res
        self.backtrack(0, digits, [])
        return self.res
                

            
