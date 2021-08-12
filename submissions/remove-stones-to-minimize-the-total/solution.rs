use std::collections::BinaryHeap;

impl Solution {
    pub fn min_stone_sum(piles: Vec<i32>, k: i32) -> i32 {
        let mut max_heap = BinaryHeap::new();
        for i in 0..piles.len() {
            max_heap.push(piles[i]);
        }
        for i in 0..(k as usize) {
            let mut v = max_heap.pop().unwrap();
            v = v - v / 2;
            max_heap.push(v);
        }
        
        let mut res = 0;
        let n = max_heap.len();
        for i in 0..n {
            res += max_heap.pop().unwrap();
        }
        return res;
        
    }
}
