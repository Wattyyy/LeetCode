impl Solution {
    fn dfs(r: usize, c: usize, grid: &Vec<Vec<char>>, visited: &mut Vec<Vec<bool>>) {
        visited[r][c] = true;
        // right
        if c + 1 < grid[0].len() && !visited[r][c + 1] && grid[r][c + 1] == '1' {
            Self::dfs(r, c + 1, grid, visited);
        }
        // up
        if 1 <= r && !visited[r - 1][c] && grid[r - 1][c] == '1' {
            Self::dfs(r - 1, c, grid, visited);
        }
        // left
        if 1 <= c && !visited[r][c - 1] && grid[r][c - 1] == '1' {
            Self::dfs(r, c - 1, grid, visited);
        }
        // down
        if r + 1 < grid.len() && !visited[r + 1][c] && grid[r + 1][c] == '1' {
            Self::dfs(r + 1, c, grid, visited);
        }
        return;
    }

    pub fn num_islands(grid: Vec<Vec<char>>) -> i32 {
        let mut visited = vec![vec![false; grid[0].len()]; grid.len()];
        let mut ans = 0;
        for r in 0..grid.len() {
            for c in 0..grid[0].len() {
                if grid[r][c] == '1' && !visited[r][c] {
                    Self::dfs(r, c, &grid, &mut visited);
                    ans += 1;
                }
            }
        }

        return ans;
    }
}


