// https://leetcode.com/problems/min-cost-climbing-stairs

use std::cmp::min;

impl Solution {
    pub fn min_cost_climbing_stairs(cost: Vec<i32>) -> i32 {
        let mut dp = vec![0; cost.len()];
        dp[0] = cost[0];
        dp[1] = cost[1];
        for (i, val) in cost.iter().enumerate(){
            if i < 2{
                continue
            }
            dp[i] = min(dp[i-2] + val, dp[i-1] + val)
        }
        return min(dp[cost.len()-1], dp[cost.len()-2])
    }
}