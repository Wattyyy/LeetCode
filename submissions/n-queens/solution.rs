impl Solution {
    fn is_valid(r: usize, c: usize, used: &Vec<(i32, i32)>) -> bool {
        let mut res = true;
        for (used_r, used_c) in used {
            let diff_r = (used_r - (r as i32)).abs();
            let diff_c = (used_c - (c as i32)).abs();
            if diff_r == 0 || diff_c == 0 || diff_r == diff_c {
                res = false;
                break;
            }
        }
        return res;
    }

    fn backtrack(
        board: &mut Vec<Vec<char>>,
        result: &mut Vec<Vec<String>>,
        used: &mut Vec<(i32, i32)>,
        r: usize,
        n: usize,
    ) {
        if r == n {
            let tmp = board.clone();
            let v: Vec<String> = tmp
                .into_iter()
                .map(|x| x.into_iter().collect::<String>())
                .collect();
            result.push(v);
            return;
        }

        for c in 0..n {
            if Self::is_valid(r, c, used) {
                used.push((r as i32, c as i32));
                board[r][c] = 'Q';
                Self::backtrack(board, result, used, r + 1, n);
                board[r][c] = '.';
                used.pop();
            }
        }
    }
    pub fn solve_n_queens(n: i32) -> Vec<Vec<String>> {
        let mut result: Vec<Vec<String>> = Vec::new();
        let mut used: Vec<(i32, i32)> = Vec::new();
        let mut board = vec![vec!['.'; n as usize]; n as usize];
        Self::backtrack(&mut board, &mut result, &mut used, 0, n as usize);
        return result;
    }
}

