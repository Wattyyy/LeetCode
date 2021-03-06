# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from collections import defaultdict

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        idx2node = defaultdict(ListNode)
        cur = head
        idx = 0
        while cur:
            idx2node[idx] = cur
            idx += 1
            cur = cur.next
        end_idx = idx - 1
        if end_idx + 1 == n:
            return head.next
        elif n == 1:
            last =  idx2node[end_idx - 1]
            last.next = None
            return head
        else:
            prev = idx2node[end_idx - n]
            prev.next = idx2node[end_idx - n + 2]
            return head
            
        

