impl Solution {
    pub fn is_ugly(n: i32) -> bool {
        if n <= 0 {
            return false;
        }
        let mut num = n;
        let factors = vec![2, 3, 5];
        for d in factors.iter() {
            while num % *d == 0 {
                num = num / *d;
            }
        }
        return num == 1;
    }
}
