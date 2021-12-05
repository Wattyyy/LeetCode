# https://leetcode.com/problems/swap-nodes-in-pairs

# https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        if head is None:
            return None
        if head.next is None:
            return head
        first = head
        second = head.next
        third = second.next
        
        second.next = first
        first.next = self.swapPairs(third)
        
        return second
        
        
        