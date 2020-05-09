# https://leetcode.com/problems/basic-calculator/submissions/

class Solution:
    def __init__(self):
        self.digits = {str(i) for i in range(10)}


    def eval_digit(self, s, index):
        res = 0
        while (index < len(s)) and (s[index] in self.digits):
            res *= 10
            res += int(s[index])
            index += 1
        return res, index - 1


    def eval_bracket(self, s, index):
        top = 0
        coef = 1
        index += 1
        while s[index] != ')':
            if s[index] == '+':
                coef = 1
            elif s[index] == '-':
                coef = -1
            elif s[index] == '(':
                res, idx = self.eval_bracket(s, index)
                top += coef * res
                index = idx
            else:
                res, idx = self.eval_digit(s, index)
                top += coef * res
                index = idx
            index += 1
        return top, index

    
    def calculate(self, s):
        s = s.replace(' ', '')
        top = 0
        index = 0
        coef = 1
        while index < len(s):
            if s[index] == '+':
                coef = 1
            elif s[index] == '-':
                coef = -1
            elif s[index] == '(':
                res, idx = self.eval_bracket(s, index)
                top += coef * res
                index = idx
            else:
                res, idx = self.eval_digit(s, index)
                top += coef * res
                index = idx
            index += 1
        return top

