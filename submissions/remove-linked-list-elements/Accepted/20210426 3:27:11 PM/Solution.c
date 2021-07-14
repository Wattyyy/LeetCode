// https://leetcode.com/problems/remove-linked-list-elements

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* removeElements(struct ListNode* head, int val){
    struct ListNode *array[10001];
    for (int i=0; i<10001; i++){
        array[i] = malloc(sizeof(struct ListNode));
    };
    struct ListNode *cur = head;
    int cnt = 0;
    while (cur!=NULL){
        if (cur->val != val){
            array[cnt] = cur;
            cnt = cnt + 1;
        }
        cur = cur->next;   
    }
    if (cnt == 0){
        return NULL;
    }
    for (int i=0; i<cnt; i++){
        if (i != cnt-1){
        array[i]->next = array[i+1];
        }
        else {
            array[i]->next = NULL;
        }
    }
    return array[0];
}