use std::collections::VecDeque;

impl Solution {
    pub fn shortest_path_binary_matrix(grid: Vec<Vec<i32>>) -> i32 {
        let (r_len, c_len) = (grid.len(), grid[0].len());
        if grid[0][0] == 1 || grid[r_len - 1][c_len - 1] == 1 {
            return -1;
        }
        let mut dist = vec![vec![i32::MAX; c_len]; r_len];
        dist[0][0] = 1;
        let mut queue: VecDeque<(usize, usize)> = VecDeque::new();
        queue.push_back((0, 0));

        while let Some((r, c)) = queue.pop_front() {
            let cnt = dist[r][c];
            for (dr, dc) in vec![
                (1, 0),
                (1, 1),
                (0, 1),
                (-1, 1),
                (-1, 0),
                (-1, -1),
                (0, -1),
                (1, -1),
            ] {
                let nr = r as i32 + dr;
                let nc = c as i32 + dc;
                if 0 <= nr
                    && nr < r_len as i32
                    && 0 <= nc
                    && nc < c_len as i32
                    && cnt + 1 < dist[nr as usize][nc as usize]
                    && grid[nr as usize][nc as usize] != 1
                {
                    dist[nr as usize][nc as usize] = cnt + 1;
                    queue.push_back((nr as usize, nc as usize));
                }
            }
        }

        if dist[r_len - 1][c_len - 1] == i32::MAX {
            return -1;
        }
        return dist[r_len - 1][c_len - 1];
    }
}

