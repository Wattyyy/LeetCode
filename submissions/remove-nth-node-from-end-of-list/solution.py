# https://leetcode.com/problems/remove-nth-node-from-end-of-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        size = 0
        cur = head
        while cur:
            size += 1
            cur = cur.next

        target = size - n + 1
        if target == 1:
            return head.next
        ptr = 2
        prev, cur = head, head.next
        while cur:
            if ptr == target:
                prev.next = cur.next
                break
            prev = cur
            cur = cur.next
            ptr += 1
        return head

        return head
