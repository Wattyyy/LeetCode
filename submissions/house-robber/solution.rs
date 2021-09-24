use std::cmp::max;
impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
        if nums.len() == 1 {
            return nums[0];
        }
        let mut dp = vec![0; nums.len()];
        dp[0] = nums[0];
        dp[1] = max(nums[0], nums[1]);
        for i in 2..nums.len() {
            dp[i] = max(dp[i-2] + nums[i], dp[i-1]);
        }
        return dp[nums.len() - 1];
        
    }
}
