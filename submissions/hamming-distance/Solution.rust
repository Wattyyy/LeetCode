// https://leetcode.com/problems/hamming-distance

impl Solution {
    pub fn hamming_distance(x: i32, y: i32) -> i32 {
        let mut tmp = x ^ y;
        let mut res = 0;
        while 0 < tmp {
            if (tmp & 1) == 1 {
                res += 1;
            }
            tmp = tmp >> 1;
        };
        return res
    }
}