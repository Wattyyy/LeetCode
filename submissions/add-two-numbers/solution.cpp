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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
      ListNode* cur1 = l1;
      ListNode* cur2 = l2;
      ListNode* head = new ListNode();
      ListNode* cur = head;

      int carry = 0;
      while (cur1 != nullptr || cur2 != nullptr) {
        int v = carry;
        if (cur1 != nullptr) {
          v = v + cur1->val;
          cur1 = cur1->next;
        }
        if (cur2 != nullptr) {
          v = v + cur2->val;
          cur2 = cur2->next;
        }
        
        cur->val = (v % 10);
        carry = v / 10;
        if (cur1 == nullptr && cur2 == nullptr) {
          if (carry == 1) {
            cur->next = new ListNode(1);
          }
          break;
        }
        else {
          cur->next = new ListNode();
          cur = cur->next;
        }
      }

      return head;
    }
};


