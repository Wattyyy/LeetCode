use std::cmp::min;

impl Solution {
    pub fn num_squares(n: i32) -> i32 {
        let mut dp = vec![10001; 10001];
        for i in 0..101 {
            dp[i * i] = 1;
        }
        for i in 1..((n + 1) as usize) {
            for j in 1..101 {
                let k = j * j;
                if k < i {
                    dp[i] = min(dp[i - k] + 1, dp[i]);
                }
                else {
                    break;
                }
            }
        }
        return dp[n as usize];
    }
}
