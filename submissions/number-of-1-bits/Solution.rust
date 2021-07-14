// https://leetcode.com/problems/number-of-1-bits

impl Solution {
    pub fn hammingWeight (n: u32) -> i32 {
        let mut res = 0;
        let mut tmp = n;
        while 0 < tmp {
            if tmp & 1 == 1 {
                res += 1;
            }
            tmp = tmp >> 1;
        }
        return res
    }
}