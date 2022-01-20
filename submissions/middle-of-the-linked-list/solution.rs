// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
// 
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }

impl Solution {
    pub fn middle_node(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        if head.is_none() {
            return None;
        }
        
        let mut cur = &head;
        let mut length = 0;
        while let Some(node) = cur {
            length += 1;
            cur = &node.next;
        }

        let mut cur = &head;
        let mut cnt = 0;
        while let Some(node) = cur {
            if cnt == (length / 2) {
                return cur.clone();
            }
            cnt += 1;
            cur = &node.next;
        }

        return None;
        
    }
}


