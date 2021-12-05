# https://leetcode.com/problems/add-two-numbers-ii

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from collections import deque


class Solution:
    def addTwoNumbers(self, l1, l2):
        if not l1 and not l2:
            return None
        st1, st2 = [], []
        cur1 = l1
        while cur1:
            st1.append(cur1.val)
            cur1 = cur1.next
        cur2 = l2
        while cur2:
            st2.append(cur2.val)
            cur2 = cur2.next

        add_one = False
        sum_ls = deque([])
        while st1 or st2:

            if st1 and st2:
                val = st1.pop(-1) + st2.pop(-1)
            elif not st1:
                val = st2.pop(-1)
            else:
                val = st1.pop(-1)

            if add_one:
                val += 1
            if 10 <= val:
                add_one = True
            else:
                add_one = False
            sum_ls.appendleft(val % 10)

        if add_one:
            sum_ls.appendleft(1)
        head = ListNode(sum_ls[0])
        cur = head
        for i in range(1, len(sum_ls)):
            cur.next = ListNode(sum_ls[i])
            cur = cur.next
        return head
