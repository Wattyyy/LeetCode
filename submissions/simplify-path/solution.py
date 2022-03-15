import re


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for name in re.split(r"/", path):
            if name == "" or name == ".":
                continue
            if name == "..":
                if 0 < len(stack):
                    stack.pop()
            else:
                stack.append(name)

        if len(stack) == 0:
            return "/"
        else:
            res = "/" + "/".join(stack)
            return res

