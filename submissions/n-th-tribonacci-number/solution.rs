impl Solution {
    pub fn tribonacci(n: i32) -> i32 {
        let mut dp = vec![0; 38];
        for i in 1..38 {
            if i < 3 {
                dp[i] = 1;
            }
            else {
                dp[i] = dp[i-1] + dp[i-2] + dp[i-3];
            }
        }
        return dp[n as usize];
    }
}
