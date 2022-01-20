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

class Solution {
    list: Array<number>;

    constructor(head: ListNode | null) {
        this.list = new Array();
        let cur: ListNode | null = head;
        while (cur !== null) {
            this.list.push(cur.val);
            cur = cur.next;
        }
    }

    getRandom(): number {
        let idx = Math.floor(Math.random() * this.list.length);
        return this.list[idx];
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(head)
 * var param_1 = obj.getRandom()
 */
