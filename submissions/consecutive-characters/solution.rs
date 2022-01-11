use std::cmp::max;

impl Solution {
    pub fn max_power(s: String) -> i32 {
        let bytes = s.as_bytes();
        let mut cnt = 1;
        let mut ans = 1;
        let mut prev = bytes[0];
        for i in 1..bytes.len() {
            if bytes[i] == prev {
                cnt += 1;
            } else {
                prev = bytes[i];
                ans = max(cnt, ans);
                cnt = 1;
            }
        }
        ans = max(cnt, ans);
        return ans;
    }
}


