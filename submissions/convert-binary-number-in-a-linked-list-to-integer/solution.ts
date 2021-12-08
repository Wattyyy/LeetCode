/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function getDecimalValue(head: ListNode | null): number {
    let ans = 0;
    let cur: ListNode | null = head;
    while (cur !== null) {
        ans = ans << 1;
        ans = ans | cur.val;
        cur = cur.next;
    }
    
    return ans;
};
