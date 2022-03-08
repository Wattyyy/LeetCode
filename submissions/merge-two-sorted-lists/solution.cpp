class Solution
{
public:
  ListNode *mergeTwoLists(ListNode *list1, ListNode *list2)
  {
    if (list2 == nullptr)
    {
      return list1;
    }
    if (list1 == nullptr)
    {
      return list2;
    }

    ListNode *cur1 = list1;
    ListNode *cur2 = list2;
    ListNode *cur;
    if (cur1->val < cur2->val)
    {
      cur = cur1;
      cur1 = cur1->next;
    }
    else
    {
      cur = cur2;
      cur2 = cur2->next;
    }
    while (cur1 != nullptr || cur2 != nullptr)
    {
      if (cur2 == nullptr)
      {
        cur->next = cur1;
        cur1 = cur1->next;
        cur = cur->next;
      }
      else if (cur1 == nullptr)
      {
        cur->next = cur2;
        cur2 = cur2->next;
        cur = cur->next;
      }
      else
      {
        if (cur1->val < cur2->val)
        {
          cur->next = cur1;
          cur1 = cur1->next;
          cur = cur->next;
        }
        else
        {
          cur->next = cur2;
          cur2 = cur2->next;
          cur = cur->next;
        }
      }
    }
    cur->next = nullptr;
    if (list1->val < list2->val)
    {
      return list1;
    }
    else
    {
      return list2;
    }
  }
};
