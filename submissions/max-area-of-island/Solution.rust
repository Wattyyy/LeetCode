// https://leetcode.com/problems/max-area-of-island

use std::collections::VecDeque;
use std::collections::HashSet;
use std::cmp::max;

impl Solution {
    pub fn max_area_of_island(grid: Vec<Vec<i32>>) -> i32 {
        let mut queue: VecDeque<(i32, i32)> = VecDeque::with_capacity(2500);
        let mut visited: HashSet<(i32, i32)> = HashSet::with_capacity(2500);
        let (R, C) = (grid.len() as i32, grid[0].len() as i32);
        let mut ans = 0;
        
        for r in 0..R {
            for c in 0..C {
                if grid[r as usize][c as usize] == 1 && !visited.contains(&(r, c)){
                    queue.push_back((r, c));
                    visited.insert((r, c));
                    let mut tmp = 1;
                    while 0 < queue.len() {
                        let (y, x) = queue.pop_front().unwrap();
                        let next_vec: Vec<(i32, i32)> = vec![(y+1, x), (y-1, x), (y, x+1), (y, x-1)];
                        for (ny, nx) in next_vec.iter(){
                            if 0 <= *ny && *ny < R && 0 <= *nx && *nx < C && grid[*ny as usize][*nx as usize] == 1 && !visited.contains(&(*ny, *nx)) {
                                tmp += 1;
                                visited.insert((*ny, *nx));
                                queue.push_back((*ny, *nx))
                            }
                        }
                    }
                    ans = max(ans, tmp);
                }
            }
        }
    return ans 
    }
}