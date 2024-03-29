// https://leetcode.com/problems/gray-code

impl Solution {
    pub fn gray_code(n: i32) -> Vec<i32> {
        let mut res = Vec::new();
        let x: u32 = 2;
        for i in 0..x.pow(n as u32) {
            let num = i as i32;
            res.push( (num >> 1) ^ num );
        }
        return res
    }
}