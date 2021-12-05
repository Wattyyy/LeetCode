# https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        queue1, queue2 = deque([]), deque([])
        cur = l1
        while cur:
            queue1.append(cur.val)
            cur = cur.next
        cur = l2
        while cur:
            queue2.append(cur.val)
            cur = cur.next

        vals = []
        while queue1 or queue2:
            v1, v2 = 0, 0
            if queue1:
                v1 = queue1.popleft()
            if queue2:
                v2 = queue2.popleft()
            vals.append(v1 + v2)

        N = len(vals)
        for i in range(N):
            if i == N - 1:
                if 10 <= vals[i]:
                    vals[i] = vals[i] % 10
                    vals.append(1)
            else:
                if 10 <= vals[i]:
                    vals[i] = vals[i] % 10
                    vals[i + 1] += 1

        head = ListNode(vals[0])
        cur = head
        for i, v in enumerate(vals):
            if i == 0:
                continue
            cur.next = ListNode(v)
            cur = cur.next
        return head
