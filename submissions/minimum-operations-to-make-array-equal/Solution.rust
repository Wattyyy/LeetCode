// https://leetcode.com/problems/minimum-operations-to-make-array-equal

impl Solution {
    pub fn min_operations(n: i32) -> i32 {
        let mut res = 0;
        let mut val = 0;
        if n % 2 == 1{
            val = 2;
        }
        else{
            val = 1;
        }
        let end = n / 2;
        for x in 0..end{
            res += val;
            val += 2;
        }
        res
        
        
    }
}