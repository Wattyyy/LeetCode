# https://leetcode.com/problems/string-to-integer-atoi

class Solution:
    def myAtoi(self, str):
        if not str:
            return 0
        nums = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
        ans = []
        eval_num = False
        is_minus = False
        for s in str:
            if eval_num:
                if s not in nums:
                    break
                else:
                    ans.append(s)
            else:
                if s == " ":
                    continue
                elif s == "-":
                    is_minus = True
                    eval_num = True
                elif s == "+":
                    eval_num = True
                elif s in nums:
                    ans.append(s)
                    eval_num = True
                else:
                    return 0
        try:
            val = int("".join(ans))
            if is_minus:
                val = -1 * val
                if val < -2**31:
                    return -2**31
                else:
                    return val
            else:
                if 2**31 - 1 < val:
                    return 2**31 - 1
                else:
                    return val
        except:
            return 0
        