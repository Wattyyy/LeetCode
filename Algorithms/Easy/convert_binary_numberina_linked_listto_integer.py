# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/submissions/

class Solution:
    def getDecimalValue(self, head):
        bin_list = []
        node = head
        while node:
            bin_list.append(node.val)
            node = node.next
        L = len(bin_list)
        ans = 0
        for i in range(L):
            ans += bin_list[i]*2**(L-1-i)
        return ans
            
        
