# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head):
        if not head:
            return None
        stack = []
        cur = head
        while cur:
            if cur.child:
                stack.append(cur.next)
                cur.next = cur.child
                cur.next.prev = cur
                cur = cur.next
                cur.prev.child = None
            elif not cur.next:
                if not stack:
                    break
                else:
                    node = stack.pop(-1)
                    cur.next = node
                    if node:
                        cur.next.prev = cur
                    cur = cur.next
            else:
                cur = cur.next
        return head

            

            

        