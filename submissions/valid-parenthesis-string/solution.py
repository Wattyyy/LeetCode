# https://leetcode.com/problems/valid-parenthesis-string


class Solution:
    def checkValidString(self, s):
        stack = []
        for char in s:
            if char == "*" or char == "(":
                stack.append(char)

            elif char == ")":
                idx = len(stack) - 1
                while 0 <= idx:
                    if stack[idx] == "*":
                        idx -= 1
                        continue
                    elif stack[idx] == "(":
                        del stack[idx]
                        break
                    else:
                        stack.append(char)
                        break
                if idx == -1:
                    stack.append(char)

        while 1 < len(stack):
            flag = False
            stack_set = set(stack)
            if (len(stack_set) == 1) and ("*" in stack_set):
                return True

            for i in range(len(stack) - 1):
                if stack[i : i + 2] == ["*", ")"] or stack[i : i + 2] == ["(", "*"]:
                    del stack[i + 1]
                    del stack[i]
                    flag = True
                    break

            if not flag:
                return False

        stack_set = set(stack)
        if "(" not in stack_set and ")" not in stack_set:
            return True
        else:
            return False
