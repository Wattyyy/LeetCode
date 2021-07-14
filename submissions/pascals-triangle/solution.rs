// https://leetcode.com/problems/pascals-triangle

impl Solution {
    pub fn generate(num_rows: i32) -> Vec<Vec<i32>> {
        if num_rows == 1 {
            return vec![vec![1]];
        }
        if num_rows == 2 {
            return vec![vec![1], vec![1,1]] 
        }
        
        let mut res = vec![vec![1], vec![1,1]];
        for i in 2..num_rows {
            let mut new_vec = Vec::new();
            let idx = i as usize;
            for j in 0..res[idx-1].len() {
                if j == 0 {
                    new_vec.push(1);
                }
                else {
                    let val = res[idx-1][j-1] + res[idx-1][j];
                    new_vec.push(val);
                }
            }
            new_vec.push(1);
            res.push(new_vec.clone());
        }
        return res
    }
}