use std::char;
use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn backtrack(
        idx: usize,
        flag: &mut bool,
        board: &mut Vec<Vec<char>>,
        rows: &Vec<usize>,
        cols: &Vec<usize>,
        grid_hm: &mut HashMap<(usize, usize), HashSet<char>>,
        row_hm: &mut HashMap<usize, HashSet<char>>,
        col_hm: &mut HashMap<usize, HashSet<char>>,
    ) {
        if idx == rows.len() {
            *flag = true;
            return;
        }
        let (r, c) = (rows[idx], cols[idx]);
        for num in 1..10 {
            let ch = char::from_digit(num, 10).unwrap();
            if !grid_hm[&(r / 3, c / 3)].contains(&ch)
                && !row_hm[&r].contains(&ch)
                && !col_hm[&c].contains(&ch)
            {
                grid_hm.get_mut(&(r / 3, c / 3)).unwrap().insert(ch);
                row_hm.get_mut(&r).unwrap().insert(ch);
                col_hm.get_mut(&c).unwrap().insert(ch);
                board[r][c] = ch;
                Self::backtrack(idx + 1, flag, board, rows, cols, grid_hm, row_hm, col_hm);
                if *flag {
                    return;
                }
                board[r][c] = '.';
                col_hm.get_mut(&c).unwrap().remove(&ch);
                row_hm.get_mut(&r).unwrap().remove(&ch);
                grid_hm.get_mut(&(r / 3, c / 3)).unwrap().remove(&ch);
            }
        }
    }

    pub fn solve_sudoku(board: &mut Vec<Vec<char>>) {
        let mut grid_hm: HashMap<(usize, usize), HashSet<char>> = HashMap::new();
        let mut row_hm: HashMap<usize, HashSet<char>> = HashMap::new();
        let mut col_hm: HashMap<usize, HashSet<char>> = HashMap::new();
        let mut rows: Vec<usize> = Vec::new();
        let mut cols: Vec<usize> = Vec::new();
        for r in 0..9 {
            for c in 0..9 {
                grid_hm.entry((r / 3, c / 3)).or_insert_with(HashSet::new);
                row_hm.entry(r).or_insert_with(HashSet::new);
                col_hm.entry(c).or_insert_with(HashSet::new);
                let key = board[r][c];
                if key == '.' {
                    rows.push(r);
                    cols.push(c);
                } else {
                    grid_hm.get_mut(&(r / 3, c / 3)).unwrap().insert(key);
                    row_hm.get_mut(&r).unwrap().insert(key);
                    col_hm.get_mut(&c).unwrap().insert(key);
                }
            }
        }
        let mut flag = false;
        Self::backtrack(
            0,
            &mut flag,
            board,
            &rows,
            &cols,
            &mut grid_hm,
            &mut row_hm,
            &mut col_hm,
        );
        return;
    }
}


