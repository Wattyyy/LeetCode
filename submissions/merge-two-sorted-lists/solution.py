// https://leetcode.com/problems/merge-two-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1 is None and l2 is None:
            return None
        else:
            if l1.val > l2.val:
                nx = l2.next 
                l2.next = self.mergeTwoLists(l1, nx)
                return l2
            else:
                nx = l1.next
                l1.next = self.mergeTwoLists(nx, l2)
                return l1
        