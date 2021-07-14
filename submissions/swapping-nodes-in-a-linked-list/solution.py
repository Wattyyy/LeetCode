// https://leetcode.com/problems/swapping-nodes-in-a-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        length = 0
        cur_node = head
        while cur_node:
            length += 1
            cur_node = cur_node.next
        
        cnt = 0
        cur_node = head
        while cur_node:
            cnt += 1
            if cnt == k:
                val1 = cur_node.val
            if cnt == length + 1 - k:
                val2 = cur_node.val
            cur_node = cur_node.next
        
        cnt = 0
        cur_node = head
        while cur_node:
            cnt += 1
            if cnt == k:
                cur_node.val = val2
            if cnt == length + 1 - k:
                cur_node.val = val1
            cur_node = cur_node.next
        
        return head
        
        
        
            
            
        