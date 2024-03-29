// https://leetcode.com/problems/reshape-the-matrix

impl Solution {
    pub fn matrix_reshape(mat: Vec<Vec<i32>>, r: i32, c: i32) -> Vec<Vec<i32>> {
        let V = mat.len();
        let H = mat[0].len();
        let area = (r * c) as usize;
        if V * H == area {
            let mut res:Vec<Vec<i32>> = Vec::new();
            let mut tmp:Vec<i32> = Vec::new();
            for v in 0..V {
                for h in 0..H {
                    tmp.push(mat[v][h]);
                    if tmp.len() == (c as usize) {
                        res.push(tmp.clone());
                        tmp.clear();
                    }
                }
            }
            return res
            
        }
        else {
            return mat
        }
    }
}