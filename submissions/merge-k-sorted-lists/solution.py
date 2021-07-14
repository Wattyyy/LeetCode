// https://leetcode.com/problems/merge-k-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq
class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None
        min_heap = []
        heapq.heapify(min_heap)
        for i, node in enumerate(lists):
            cur = node
            while cur:
                heapq.heappush(min_heap, (cur.val, i))
                cur = cur.next
        if not min_heap:
            return None
        head_val, _ = heapq.heappop(min_heap)
        head = ListNode(head_val)
        cur = head
        while min_heap:
            node_val, _ = heapq.heappop(min_heap)
            cur.next = ListNode(node_val)
            cur = cur.next
        return head
