use std::cmp::max;

impl Solution {
    pub fn stone_game(piles: Vec<i32>) -> bool {
        let n = piles.len();
        let mut dp = vec![vec![0; n]; n];
        for i in (0..n).rev() {
            for j in i..n {
                if i == j {
                    dp[i][j] = piles[i];
                } else {
                    dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1]);
                }
            }
        }
        return 0 < dp[0][n - 1];
    }
}



