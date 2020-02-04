# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        if head is None:
            return None
        if head.next is None:
            return head
        next_node = head.next
        head.next = None
        def helper(node, head):
            nx = node.next
            if nx is None:
                node.next = head
                return node
            else:
                node.next = head
                return helper(nx, node)
        
        return helper(next_node, head)
