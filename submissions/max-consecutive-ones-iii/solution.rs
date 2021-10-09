use std::cmp::max;

impl Solution {
    pub fn longest_ones(nums: Vec<i32>, k: i32) -> i32 {
        let mut sp = 0 as usize;
        let mut ans = 0;
        let mut replace = 0;
        for ep in 0..nums.len() {
            if nums[ep] == 0 {
                replace += 1;
            }
            while k < replace {
                if nums[sp] == 0 {
                    replace -= 1
                }
                sp += 1;
            }
            ans = max(ans, (ep - sp + 1) as i32);
        }
        return ans;
    }
}
