use std::cmp::max;
use std::collections::VecDeque;

impl Solution {
    pub fn calculate_minimum_hp(dungeon: Vec<Vec<i32>>) -> i32 {
        let mut ans = 40000001;

        let row_len = dungeon.len();
        let col_len = dungeon[0].len();

        let mut left = 1;
        let mut right = 40000001;
        while left <= right {
            let mid = (left + right) / 2;

            // init life_table
            let mut life_table = vec![vec![-40000001; col_len]; row_len];
            for r in 0..row_len {
                for c in 0..col_len {
                    if r == 0 && c == 0 {
                        life_table[0][0] = mid + dungeon[0][0];
                    } else if r == 0 {
                        let life = life_table[r][c - 1] + dungeon[r][c];
                        if 0 < life {
                            life_table[r][c] = life;
                        }
                    } else if c == 0 {
                        let life = life_table[r - 1][c] + dungeon[r][c];
                        if 0 < life {
                            life_table[r][c] = life;
                        }
                    } else {
                        let life = max(
                            life_table[r - 1][c] + dungeon[r][c],
                            life_table[r][c - 1] + dungeon[r][c],
                        );
                        if 0 < life {
                            life_table[r][c] = life;
                        }
                    }
                }
            }

            // check whether the knight can reach the bottom-right corner
            let mut visited = vec![vec![false; col_len]; row_len];
            let mut queue: VecDeque<(usize, usize)> = VecDeque::new();
            if 0 < life_table[0][0] {
                queue.push_back((0, 0));
                visited[0][0] = true;
            }
            while 0 < queue.len() {
                let tp = queue.pop_front().unwrap();
                let r = tp.0;
                let c = tp.1;
                if r + 1 < row_len && 0 < life_table[r + 1][c] && !visited[r + 1][c] {
                    queue.push_back((r + 1, c));
                    visited[r + 1][c] = true;
                }
                if c + 1 < col_len && 0 < life_table[r][c + 1] && !visited[r][c + 1] {
                    queue.push_back((r, c + 1));
                    visited[r][c + 1] = true;
                }
            }
            if visited[row_len - 1][col_len - 1] {
                ans = mid;
                right = mid - 1;
            } else {
                left = mid + 1
            }
        }

        return ans;
    }
}


