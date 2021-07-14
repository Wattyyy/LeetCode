// https://leetcode.com/problems/maximum-erasure-value

use std::collections::HashSet;
use std::cmp;

impl Solution {
    pub fn maximum_unique_subarray(nums: Vec<i32>) -> i32 {
        if nums.len() == 1 {
            return nums[0]
        }
        let (mut l, mut r) = (0, 1);
        let (mut ans, mut tmp) = (nums[0], nums[0]);
        let mut used = HashSet::with_capacity(nums.len());
        used.insert(nums[0]);
        while r < nums.len(){
            let r_num = nums[r];
            while used.contains(&r_num){
                let l_num = nums[l];
                used.remove(&l_num);
                tmp -= l_num;
                l += 1;
            }
            used.insert(r_num);
            tmp += r_num;
            ans = cmp::max(tmp, ans);
            r += 1;
        }
        return ans
    }
}