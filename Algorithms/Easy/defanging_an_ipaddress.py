# https://leetcode.com/problems/defanging-an-ip-address/submissions/

class Solution:
    def defangIPaddr(self, address):
        if not address:
            return ""
        ls = address.split(".")
        return "[.]".join(ls)
