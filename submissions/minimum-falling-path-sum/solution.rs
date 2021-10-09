use std::cmp::min;
impl Solution {
    pub fn min_falling_path_sum(matrix: Vec<Vec<i32>>) -> i32 {
        let row_len = matrix.len();
        let col_len = matrix[0].len();
        let mut dp = vec![vec![0; col_len]; row_len];
        for r in 0..row_len {
            for c in 0..col_len {
                if r == 0 {
                    dp[r][c] = matrix[r][c];
                    continue;
                }
                if c == 0 {
                    dp[r][c] = min(dp[r - 1][c], dp[r - 1][c + 1]) + matrix[r][c];
                } else if c == col_len - 1 {
                    dp[r][c] = min(dp[r - 1][c - 1], dp[r - 1][c]) + matrix[r][c];
                } else {
                    dp[r][c] =
                        min(min(dp[r - 1][c - 1], dp[r - 1][c]), dp[r - 1][c + 1]) + matrix[r][c];
                }
            }
        }
        return *dp[row_len - 1].iter().min().unwrap();
    }
}
