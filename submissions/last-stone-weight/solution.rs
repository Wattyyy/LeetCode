use std::collections::BinaryHeap;

impl Solution {
    pub fn last_stone_weight(stones: Vec<i32>) -> i32 {
        let mut max_heap = BinaryHeap::from(stones);
        while 2 <= max_heap.len() {
            let v1 = max_heap.pop().unwrap();
            let v2 = max_heap.pop().unwrap();
            let diff = (v1 - v2).abs();
            if diff != 0 {
                max_heap.push(diff);
            }
        }
        let res = max_heap.pop();
        match res {
            Some(res) => res,
            None => 0
        }
    }
}

