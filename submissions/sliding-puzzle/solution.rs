use std::collections::VecDeque;

impl Solution {
    pub fn hashing(board: &Vec<Vec<i32>>) -> usize {
        let mut hash: usize = 0;
        for r in 0..2 {
            for c in 0..3 {
                let p = (r * 3 + c) as u32;
                hash += usize::pow(6, p) * (board[r][c] as usize);
            }
        }
        return hash;
    }

    pub fn slide(board: &Vec<Vec<i32>>) -> Vec<Vec<Vec<i32>>> {
        let mut states: Vec<Vec<Vec<i32>>> = Vec::new();

        let mut r_0: usize = 0;
        let mut c_0: usize = 0;
        for r in 0..2 {
            for c in 0..3 {
                if board[r][c] == 0 {
                    r_0 = r;
                    c_0 = c;
                    break;
                }
            }
        }

        // move right
        if c_0 != 2 {
            let mut state = board.clone();
            state[r_0][c_0] = state[r_0][c_0 + 1];
            state[r_0][c_0 + 1] = 0;
            states.push(state);
        }
        // move left
        if c_0 != 0 {
            let mut state = board.clone();
            state[r_0][c_0] = state[r_0][c_0 - 1];
            state[r_0][c_0 - 1] = 0;
            states.push(state);
        }
        // move down
        if r_0 != 1 {
            let mut state = board.clone();
            state[r_0][c_0] = state[r_0 + 1][c_0];
            state[r_0 + 1][c_0] = 0;
            states.push(state);
        }
        // move upper
        if r_0 != 0 {
            let mut state = board.clone();
            state[r_0][c_0] = state[r_0 - 1][c_0];
            state[r_0 - 1][c_0] = 0;
            states.push(state);
        }

        return states;
    }

    pub fn sliding_puzzle(board: Vec<Vec<i32>>) -> i32 {
        let mut cnt_table = vec![-1; 46656];
        cnt_table[Self::hashing(&board)] = 0;

        let mut state_queue: VecDeque<Vec<Vec<i32>>> = VecDeque::new();
        state_queue.push_back(board.clone());
        let mut cnt_queue: VecDeque<i32> = VecDeque::new();
        cnt_queue.push_back(0);
        while 0 < state_queue.len() {
            if cnt_table[7465] != -1 {
                break;
            }
            let state = state_queue.pop_front().unwrap();
            let cnt = cnt_queue.pop_front().unwrap();
            cnt_table[Self::hashing(&state)] = cnt;

            let next_states = Self::slide(&state);
            for s in next_states.iter() {
                let hash = Self::hashing(s);
                if cnt_table[hash] == -1 || cnt + 1 < cnt_table[hash] {
                    state_queue.push_back(s.clone());
                    cnt_queue.push_back(cnt + 1);
                }
            }
        }

        return cnt_table[7465];
    }
}


