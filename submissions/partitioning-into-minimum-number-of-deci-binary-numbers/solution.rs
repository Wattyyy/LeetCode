// https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers

use std::cmp;
impl Solution {
    pub fn min_partitions(n: String) -> i32 {
        let mut res = 0;
        for d in n.chars(){
            let val = d.to_digit(10).unwrap() as i32;
            res = cmp::max(val, res);
        }
        return res
    }
}