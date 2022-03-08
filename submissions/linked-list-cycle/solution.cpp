class Solution
{
public:
  bool hasCycle(ListNode *head)
  {
    ListNode *cur = head;
    int cnt = 0;
    while (cur != nullptr)
    {
      cnt += 1;
      if (10001 <= cnt)
      {
        return true;
      }
      cur = cur->next;
    }

    return false;
  }
};

