impl Solution {
    pub fn bitwise_complement(n: i32) -> i32 {
        if n == 0 {
            return 1;
        }
        let mut l = 0;
        let mut r = 31;
        let mut p = 0;
        while l <= r {
            let m = (l + r) / 2;
            if n <= (1 << m) - 1 {
                p = m;
                r = m - 1;
            } else {
                l = m + 1;
            }
        }
        return n ^ ((1 << p) - 1);
    }
}


