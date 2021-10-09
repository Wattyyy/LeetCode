use std::cmp::min;
impl Solution {
    pub fn min_path_sum(grid: Vec<Vec<i32>>) -> i32 {
        let row_len = grid.len();
        let col_len = grid[0].len();
        let mut path_sum = vec![vec![0; col_len]; row_len];
        for r in 0..row_len {
            for c in 0..col_len {
                if r == 0 && c == 0 {
                    path_sum[r][c] = grid[r][c];
                } else if r == 0 {
                    path_sum[r][c] = path_sum[r][c - 1] + grid[r][c];
                } else if c == 0 {
                    path_sum[r][c] = path_sum[r - 1][c] + grid[r][c];
                } else {
                    path_sum[r][c] = min(path_sum[r - 1][c], path_sum[r][c - 1]) + grid[r][c];
                }
            }
        }
        return path_sum[row_len - 1][col_len - 1];
    }
}


