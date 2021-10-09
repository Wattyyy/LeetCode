use std::cmp::{max, min};

impl Solution {
    pub fn max_product(nums: Vec<i32>) -> i32 {
        if nums.len() == 1 {
            return nums[0];
        }
        let mut minus_dp = vec![0; nums.len()];
        let mut plus_dp = vec![0; nums.len()];
        if nums[0] < 0 {
            minus_dp[0] = nums[0];
        }
        if 0 < nums[0] {
            plus_dp[0] = nums[0];
        }
        for i in 1..nums.len() {
            if nums[i] < 0 {
                minus_dp[i] = min(plus_dp[i - 1] * nums[i], nums[i]);
                plus_dp[i] = max(minus_dp[i - 1] * nums[i], 0);
            }
            if 0 < nums[i] {
                minus_dp[i] = min(minus_dp[i - 1] * nums[i], 0);
                plus_dp[i] = max(plus_dp[i - 1] * nums[i], nums[i]);
            }
        }

        return *plus_dp.iter().max().unwrap();
    }
}
