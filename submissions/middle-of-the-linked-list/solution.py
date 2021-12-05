# https://leetcode.com/problems/middle-of-the-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from math import ceil
from collections import defaultdict
class Solution:
    def middleNode(self, head):
        cur = head
        cnt = 1
        d = defaultdict(int)
        while cur:
            d[cnt] = cur
            cur = cur.next
            cnt += 1
        if (cnt - 1) % 2 == 0:
            key = ceil(cnt / 2)
            return d[key]
        else:
            key = cnt // 2
            return d[key]
            
        