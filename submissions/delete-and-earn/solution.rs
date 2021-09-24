use std::cmp::max;
impl Solution {
    pub fn delete_and_earn(nums: Vec<i32>) -> i32 {
        let mut points = vec![0; 10001];
        for i in 0..nums.len() {
            points[nums[i] as usize] += nums[i];
        }
        let mut dp = vec![0; 10001];
        dp[1] += points[1];
        for i in 2..10001 {
            dp[i] = max(dp[i-2] + points[i], dp[i-1]);        
        }
        return dp[10000];
    }
}        
