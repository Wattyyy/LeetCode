# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        arr = []
        cur = head
        
        if left == 1:
            for _ in range(1 + right - left):
                arr.append(cur)
                cur = cur.next
            t_node = cur
            arr = arr[::-1]
            for i in range(len(arr)):
                if i == len(arr) - 1:
                    arr[i].next = t_node
                else:
                    arr[i].next = arr[i+1]
                    
            return arr[0]
        
        prev = None
        cnt = 1
        while cur:
            if cnt == left:
                for _ in range(1 + right - left):
                    arr.append(cur)
                    cur = cur.next
                t_node = cur
                arr = arr[::-1]
                prev.next = arr[0]
                for i in range(len(arr)):
                    if i == len(arr) - 1:
                        arr[i].next = t_node
                    else:
                        arr[i].next = arr[i+1]
                return head
            
            else:
                prev = cur
                cur = cur.next
                cnt += 1
                
