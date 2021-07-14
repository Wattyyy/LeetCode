// https://leetcode.com/problems/remove-duplicates-from-sorted-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        prev = head
        cur = head.next
        while cur:
            if cur.val == prev.val:
                prev.next = cur.next
                cur = cur.next
            else:
                cur = cur.next
                prev = prev.next
        return head
                
        