# https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from heapq import *
class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None
        if len(lists)==1:
            return lists[0]
        
        head = ListNode(0)
        tail = head
        h = []
        for l in lists:
            if l is not None:
                heappush(h, (l.val, id(l), l))
    
        while h:
            val, _, node = heappop(h)
            if node.next is not None:
                heappush(h, (node.next.val, id(node.next), node.next))
            tail.next = node
            tail = node
            
        return head.next
            
