use std::cmp::max;
use std::collections::VecDeque;

impl Solution {
    pub fn oranges_rotting(grid: Vec<Vec<i32>>) -> i32 {
        let row_len = grid.len();
        let col_len = grid[0].len();
        let mut queue: VecDeque<(usize, usize, i32)> = VecDeque::new();
        let mut rotten = grid.clone();
        for r in 0..row_len {
            for c in 0..col_len {
                if grid[r][c] == 2 {
                    queue.push_back((r, c, 0));
                }
            }
        }
        let mut ans = 0;
        while 0 < queue.len() {
            let (r, c, cnt) = queue.pop_front().unwrap();
            ans = max(ans, cnt);
            if 0 < c && rotten[r][c - 1] == 1 {
                rotten[r][c - 1] = 2;
                queue.push_back((r, c - 1, cnt + 1));
            }
            if c + 1 < col_len && rotten[r][c + 1] == 1 {
                rotten[r][c + 1] = 2;
                queue.push_back((r, c + 1, cnt + 1))
            }
            if 0 < r && rotten[r - 1][c] == 1 {
                rotten[r - 1][c] = 2;
                queue.push_back((r - 1, c, cnt + 1));
            }
            if r + 1 < row_len && rotten[r + 1][c] == 1 {
                rotten[r + 1][c] = 2;
                queue.push_back((r + 1, c, cnt + 1));
            }
        }

        for r in 0..row_len {
            for c in 0..col_len {
                if rotten[r][c] == 1 {
                    return -1;
                }
            }
        }

        return ans;
    }
}


