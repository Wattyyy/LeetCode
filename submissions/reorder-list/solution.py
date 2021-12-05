# https://leetcode.com/problems/reorder-list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from collections import defaultdict
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        idx2node = defaultdict(ListNode)
        idx = 0
        cur = head
        while cur:
            idx2node[idx] = cur
            idx += 1
            cur = cur.next
        
        l, r = 0, len(idx2node) - 1
        while l < r:
            nx_node = idx2node[l].next
            idx2node[l].next = idx2node[r]
            idx2node[r].next = idx2node[l+1]
            l += 1
            r -= 1
        
        last_idx = len(idx2node) // 2
        idx2node[last_idx].next = None
        return        