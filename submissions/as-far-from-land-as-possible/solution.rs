// https://leetcode.com/problems/as-far-from-land-as-possible

use std::cmp;

impl Solution {
    pub fn max_distance(grid: Vec<Vec<i32>>) -> i32 {
        let mut water = Vec::new();
        let mut island = Vec::new();
        for r in 0..grid.len() {
            for c in 0..grid[0].len() {
                if grid[r][c] == 0 {
                    water.push(vec![r as i32, c as i32]);
                }
                else {
                    island.push(vec![r as i32, c as i32]);
                }
            }
        }
        if water.len() == 0 || island.len() == 0 {
            return -1
        }

        let mut res = 0;
        for wv in water.iter() {
            let mut tmp = 200;
            for iv in island.iter() {
                tmp = cmp::min(tmp, (wv[0] - iv[0]).abs() + (wv[1] - iv[1]).abs());
            }
            res = cmp::max(res, tmp);
        }
        return res
    }
}