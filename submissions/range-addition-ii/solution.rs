use std::cmp::min;

impl Solution {
    pub fn max_count(m: i32, n: i32, ops: Vec<Vec<i32>>) -> i32 {
        if ops.len() == 0 {
            return m * n;
        }
        let mut y_min = 40001;
        let mut x_min = 40001;
        for i in 0..ops.len() {
            y_min = min(y_min, ops[i][0]);
            x_min = min(x_min, ops[i][1]);
        }
        return x_min * y_min;
    }
}
