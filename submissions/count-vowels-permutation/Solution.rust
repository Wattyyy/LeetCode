// https://leetcode.com/problems/count-vowels-permutation

impl Solution {
    pub fn count_vowel_permutation(n: i32) -> i32 {
        let N = n as usize;
        let mut dp:Vec<Vec<i64>> = vec![vec![0; 5]; N+1];
        let M = 1000000007;
        for i in 0..5 {
            dp[1][i] = 1;
        }
        for i in 2..(N+1) {
            dp[i][0] = (dp[i-1][1] + dp[i-1][2] + dp[i-1][4]) % M;
            dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % M;
            dp[i][2] = (dp[i-1][1] + dp[i-1][3]) % M;
            dp[i][3] = dp[i-1][2] % M;
            dp[i][4] = (dp[i-1][2] + dp[i-1][3]) % M;
        }
        
        let mut res = 0;
        for i in 0..5 {
            res = (res + dp[N][i]) % M;
        }
        return res as i32
    }
}