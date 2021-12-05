# https://leetcode.com/problems/palindrome-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # check number of nodes
        ls = []
        cur = head
        while cur:
            ls.append(cur.val)
            cur = cur.next
        N = len(ls)
        for i in range(N):
            if ls[i] != ls[N - i - 1]:
                return False
        return True
