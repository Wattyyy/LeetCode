use std::collections::HashSet;

impl Solution {
    pub fn judge_square_sum(c: i32) -> bool {
        let mut squares = HashSet::new();
        let max = (c as f64).sqrt() as usize;
        for i in 0..(max+1) {
            let v = (i * i) as i32;
            squares.insert(v);
        }
        
        for i in 0..(max+1) {
            let tmp = c - ( (i * i) as i32);
            if tmp < 0 {
                break
            }
            if squares.contains(&tmp) {
                return true
            }
        }
        
        return false;
    }
}


