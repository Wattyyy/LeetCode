use std::collections::VecDeque;

impl Solution {
    pub fn min_cut(s: String) -> i32 {
        let byte_arr = s.as_bytes();
        let n = byte_arr.len();
        let mut dp = vec![vec![false; n]; n];
        for i in (0..n).rev() {
            for j in i..n {
                if i == j {
                    dp[i][j] = true;
                } else if j - i == 1 {
                    if byte_arr[i] == byte_arr[j] {
                        dp[i][j] = true;
                    }
                } else {
                    if byte_arr[i] == byte_arr[j] && dp[i + 1][j - 1] {
                        dp[i][j] = true;
                    }
                }
            }
        }
        let mut cnt_memo = vec![n as i32; n + 1];
        cnt_memo[0] = 0;
        let mut queue: VecDeque<(usize, i32)> = VecDeque::new();
        queue.push_back((0 as usize, 0));
        while 0 < queue.len() {
            let (idx, cnt) = queue.pop_front().unwrap();
            for i in 0..n {
                if dp[idx][i] {
                    if i + 1 == n {
                        return cnt;
                    }
                    if cnt + 1 < cnt_memo[i + 1] {
                        queue.push_back((i + 1, cnt + 1));
                        cnt_memo[i + 1] = cnt + 1;
                    }
                }
            }
        }
        return cnt_memo[n];
    }
}


