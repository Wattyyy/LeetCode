# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


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
            ans += bin_list[i] * 2 ** (L - 1 - i)
        return ans
