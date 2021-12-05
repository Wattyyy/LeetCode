# https://leetcode.com/problems/remove-linked-list-elements

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head, val):
        cur = head
        while cur and cur.val == val:
            cur = cur.next
        if not cur:
            return None
        res_head = cur
        prev, cur, nx = None, res_head, res_head.next
        while cur:
            if cur.val == val:
                prev.next = cur.next
                cur = cur.next
            else:
                prev, cur = cur, cur.next
            if not cur:
                break
        return res_head
        
        