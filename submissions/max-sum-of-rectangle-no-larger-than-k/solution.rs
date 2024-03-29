// https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k

use std::cmp::max;

impl Solution {
    pub fn max_sum_submatrix(matrix: Vec<Vec<i32>>, k: i32) -> i32 {
        let R = matrix.len();
        let C = matrix[0].len();
        let mut dp: Vec<Vec<i32>> = vec![vec![0; C]; R];

        for r in 0..R {
            for c in 0..C {
                if c == 0 {
                    dp[r][c] = matrix[r][c];
                }
                else {
                    dp[r][c] = dp[r][c-1] + matrix[r][c];
                }
            }
        }
        for r in 1..R {
            for c in 0..C {
                dp[r][c] = dp[r-1][c] + dp[r][c];
            }
        }


        let mut ans = std::i32::MIN;
        for r1 in 0..R {
            for r2 in r1..R {
                for c1 in 0..C {
                    for c2 in c1..C {
                        let mut val = 0;
                        if r1 == 0 && c1 == 0 {
                            val = dp[r2][c2];
                        }
                        else if r1 == 0 {
                            val = dp[r2][c2] - dp[r2][c1-1];
                        }
                        else if c1 == 0 {
                            val = dp[r2][c2] - dp[r1-1][c2];
                        }
                        else {
                            val = dp[r2][c2] - dp[r1-1][c2]  - dp[r2][c1-1] + dp[r1-1][c1-1];
                        }
                        
                        if val <= k {
                            ans = max(ans, val);
                        }
                    }
                }
            }
            
        }
        return ans

    }
}