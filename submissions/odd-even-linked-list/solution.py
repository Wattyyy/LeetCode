// https://leetcode.com/problems/odd-even-linked-list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head):
        if not head:
            return None
        odd, even = head, head.next
        even_tail = head.next
        if not even:
            return head
        while True:
            if not even.next:
                break
            odd.next = even.next
            odd = odd.next
            if not odd.next:
                even.next = None
                break
            even.next = odd.next
            even = even.next
            
        odd.next = even_tail
        return head
        