#include <stdlib.h>
#include <unordered_map>

using namespace std;


class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (head == NULL) {
          return NULL;
        }
        Node* cp_head = new Node(head->val);
        Node* node = head->next;
        Node* current = cp_head;
        unordered_map<Node*, Node*> org_to_cp;
        org_to_cp[head] = cp_head;

        while (node != NULL) {
          current->next = new Node(node->val);
          org_to_cp[node] = current->next;          
          current = current->next;
          node = node->next;
        }
        
        Node* cur = cp_head;
        while (head != NULL) {
          Node* rp = head->random;
          if (rp != NULL) {
            cur->random = org_to_cp[rp];
          }
          cur = cur->next;
          head = head->next;
        }

        return cp_head;
    }
};
