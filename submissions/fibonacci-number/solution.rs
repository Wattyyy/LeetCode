impl Solution {
    pub fn fib(n: i32) -> i32 {
        let mut dp = vec![0; 31];
        for i in 1..31 {
            if i < 3 {
                dp[i] = 1;
            }
            else {
                dp[i] = dp[i-1] + dp[i-2];
            }
        }


        return dp[n as usize];

    }
}
