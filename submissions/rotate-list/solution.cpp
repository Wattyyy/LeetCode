/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (head == nullptr || head->next == nullptr) {
          return head;
        }
        int length = 0;
        ListNode* tmp = head;
        while (tmp != nullptr) {
          length++;
          tmp = tmp->next;
        }

        int swap_cnt = k % length;
        if (swap_cnt == 0) {
          return head;
        }
        ListNode* tail = new ListNode();
        ListNode* cur = head;
        int cnt = 0;
        while (cnt != length - swap_cnt) {
          cnt++;
          if (cnt == length - swap_cnt) {
            tail = cur;
          }
          cur = cur->next;
        }
        tail->next = nullptr;
        ListNode* new_head = cur;
        while (cur->next != nullptr) {
          cur = cur->next;
        }
        cur->next = head;

        return new_head;
    }
};
