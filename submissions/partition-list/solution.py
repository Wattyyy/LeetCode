# https://leetcode.com/problems/partition-list


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        less_head = ListNode(-101)
        more_head = ListNode(-101)
        less = less_head
        more = more_head
        node = head
        while node:
            if node.val < x:
                less.next = node
                less = less.next
            else:
                more.next = node
                more = more.next
            node = node.next

        more.next = None
        less.next = more_head.next

        return less_head.next
