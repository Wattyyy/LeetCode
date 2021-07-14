// https://leetcode.com/problems/longest-consecutive-sequence

use std::collections::HashSet;
use std::cmp::max;

impl Solution {
    pub fn longest_consecutive(nums: Vec<i32>) -> i32 {
        let mut num_set:HashSet<i32> = HashSet::new();
        for num in nums.iter(){
            num_set.insert(*num);
        }
        let mut ans = 0;
        for num in &num_set {
            let mut val = num - 1;
            if !num_set.contains(&val){
                val += 2;
                let mut tmp = 1;
                while num_set.contains(&val){
                    tmp += 1;
                    val += 1;
                }
                ans = max(ans, tmp);
            }
        }
        return ans
    }
}
