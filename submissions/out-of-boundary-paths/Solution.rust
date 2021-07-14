// https://leetcode.com/problems/out-of-boundary-paths

impl Solution {
    pub fn find_paths(m: i32, n: i32, max_move: i32, start_row: i32, start_column: i32) -> i32 {
        let modulo = 1000000007;
        let mut dp: Vec<Vec<Vec<i32>>> = vec![vec![vec![0; (max_move+1) as usize]; n as usize]; m as usize];
        for mv in 1..max_move+1 {
            for r in 0..m {
                for c in 0..n{
                    let nrs: [i32; 4] = [r-1, r+1, r, r];
                    let ncs: [i32; 4] = [c, c, c-1, c+1];
                    for i in 0..4{
                        let nr = nrs[i];
                        let nc = ncs[i];
                        if 0 <= nr && nr < m && 0 <= nc && nc < n {
                            dp[r as usize][c as usize][mv as usize] += dp[nr as usize][nc as usize][(mv - 1) as usize];
                        }
                        else {
                            dp[r as usize][c as usize][mv as usize] += 1;
                        }
                        dp[r as usize][c as usize][mv as usize] %= modulo;
                    }
                    
                }
            }
        }
        return dp[start_row as usize][start_column as usize][max_move as usize] % modulo
    }
}