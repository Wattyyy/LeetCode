# https://leetcode.com/problems/insertion-sort-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from bisect import bisect_left
class Solution:
    def insertionSortList(self, head):
        if not head:
            return None
        arr = []
        cur = head
        while cur:
            val = cur.val
            idx = bisect_left(arr, val)
            arr.insert(idx, val)
            cur = cur.next
        res = ListNode(arr[0])
        cur = res
        for i, v in enumerate(arr):
            if i == 0:
                continue
            cur.next = ListNode(v)
            cur = cur.next
        return res
            
        
        
        
        