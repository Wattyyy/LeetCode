use std::cmp::max;

impl Solution {
    pub fn dfs(
        grid: &Vec<Vec<i32>>,
        idx_grid: &mut Vec<Vec<usize>>,
        r: i32,
        c: i32,
        idx: usize,
        cnt: &mut i32,
    ) {
        *cnt += 1;
        idx_grid[r as usize][c as usize] = idx;
        let nexts = vec![(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)];
        let (r_len, c_len) = (grid.len() as i32, grid[0].len() as i32);
        for i in 0..4 {
            let (nr, nc) = (nexts[i].0, nexts[i].1);
            if 0 <= nr
                && nr < r_len
                && 0 <= nc
                && nc < c_len
                && grid[nr as usize][nc as usize] == 1
                && idx_grid[nr as usize][nc as usize] == 0
            {
                Self::dfs(&grid, idx_grid, nr, nc, idx, cnt);
            }
        }
    }

    pub fn largest_island(grid: Vec<Vec<i32>>) -> i32 {
        let (r_len, c_len) = (grid.len(), grid[0].len());
        let mut idx_grid = vec![vec![0 as usize; c_len]; r_len];
        let mut idx = 1 as usize;
        let mut idx2area = vec![0; 25001];

        for r in 0..r_len {
            for c in 0..c_len {
                if grid[r][c] == 1 && idx_grid[r][c] == 0 {
                    let mut cnt = 0;
                    Self::dfs(&grid, &mut idx_grid, r as i32, c as i32, idx, &mut cnt);
                    idx2area[idx] = cnt;
                    idx += 1;
                }
            }
        }

        let mut ans = 0;
        for r in 0..r_len {
            for c in 0..c_len {
                if grid[r][c] == 0 {
                    let (y, x) = (r as i32, c as i32);
                    let mut tmp_val = 1;
                    let mut tmp_vec = Vec::new();
                    let nexts = vec![(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)];
                    for i in 0..4 {
                        let (ny, nx) = (nexts[i].0, nexts[i].1);
                        if 0 <= ny && ny < (r_len as i32) && 0 <= nx && nx < (c_len as i32) {
                            let tmp_idx = idx_grid[ny as usize][nx as usize];
                            if !tmp_vec.iter().any(|&i| i == tmp_idx) {
                                tmp_vec.push(tmp_idx);
                            }
                        }
                    }
                    for i in tmp_vec.iter() {
                        tmp_val += idx2area[*i];
                    }

                    ans = max(tmp_val, ans);
                }
            }
        }

        if ans == 0 {
            return idx2area[1]
        }
        return ans
    }
}

