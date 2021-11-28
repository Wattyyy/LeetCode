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

function removeElements(head: ListNode | null, val: number): ListNode | null {
    if (head === null) {
        return null;
    }
    let nodeList: Array<ListNode> = [];
    let curNode: ListNode | null = head;
    while (curNode !== null) {
        if (curNode.val !== val) {
            nodeList.push(curNode);
        }
        curNode = curNode.next;
    }

    if (nodeList.length === 0) {
        return null;
    }

    for (let i = 0; i < nodeList.length; i++) {
        if (i !== nodeList.length - 1) {
            nodeList[i].next = nodeList[i + 1];
        }
        else {
            nodeList[i].next = null;
        }
    }
    return nodeList[0];

};
