use std::cmp::max;

impl Solution {
    pub fn longest_common_subsequence(text1: String, text2: String) -> i32 {
        let mut vec1 = vec![0; 1];
        let mut vec2 = vec![0; 1];
        vec1.append(&mut text1.as_bytes().to_vec());
        vec2.append(&mut text2.as_bytes().to_vec());
        let mut dp = vec![vec![0; vec2.len()]; vec1.len()];

        for r in 1..vec1.len() {
            for c in 1..vec2.len() {
                if vec1[r] == vec2[c] {
                    dp[r][c] = dp[r - 1][c - 1] + 1;
                } else {
                    dp[r][c] = max(dp[r - 1][c], dp[r][c - 1]);
                }
            }
        }

        return dp[vec1.len() - 1][vec2.len() - 1];
    }
}
