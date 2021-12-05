# https://leetcode.com/problems/defanging-an-ip-address

class Solution:
    def defangIPaddr(self, address):
        if not address:
            return ""
        ls = address.split(".")
        return "[.]".join(ls)