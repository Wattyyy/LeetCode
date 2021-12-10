struct Solution;

impl Solution {
    pub fn num_tilings(n: i32) -> i32 {
        /*

        dp[0][n]
        | 0 | 1 |     | n-2 | n-1 |
        |---|---|-----|-----|-----|
        | * | * | ... | *   | *   |
        | * | * | ... | *   |     |


        dp[1][n]
        | 0 | 1 |     | n-2 | n-1 |
        |---|---|-----|-----|-----|
        | * | * | ... | *   |     |
        | * | * | ... | *   | *   |

        dp[2][n]
        | 0 | 1 |     | n-2 | n-1 |
        |---|---|-----|-----|-----|
        | * | * | ... | *   | *   |
        | * | * | ... | *   | *   |

        */
        let mut dp: Vec<Vec<i64>> = vec![vec![0; n as usize]; 3];
        if n == 1 {
            return 1;
        }
        dp[2][0] = 1;
        dp[0][1] = 1;
        dp[1][1] = 1;
        dp[2][1] = 2;

        let d: i64 = 1_000_000_000 + 7;
        for i in 2..(n as usize) {
            dp[0][i] = (dp[2][i - 2] + dp[1][i - 1]) % d;
            dp[1][i] = (dp[2][i - 2] + dp[0][i - 1]) % d;
            dp[2][i] = (dp[2][i - 2] + dp[0][i - 1] + dp[1][i - 1] + dp[2][i - 1]) % d;
        }

        return dp[2][(n as usize) - 1] as i32;
    }
}

fn main() {
    assert_eq!(5, Solution::num_tilings(3));
    assert_eq!(1, Solution::num_tilings(1));
    assert_eq!(2, Solution::num_tilings(2));
    assert_eq!(979232805, Solution::num_tilings(1000));
}

