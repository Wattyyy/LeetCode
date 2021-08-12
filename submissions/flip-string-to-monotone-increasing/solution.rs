use std::cmp::min;

impl Solution {
    pub fn min_flips_mono_incr(s: String) -> i32 {
        let arr = s.as_bytes();
        let n = arr.len();
        let mut lr_1_cnt = vec![0; n];
        let mut rl_0_cnt = vec![0; n];
        
        for i in 0..n {
            if arr[i] == b'1' {
                lr_1_cnt[i] += 1;
            }
            if 1 <= i {
                lr_1_cnt[i] += lr_1_cnt[i-1];
            }
        }
        
        for i in (0..n).rev() {
            if arr[i] == b'0' {
                rl_0_cnt[i] += 1;
            }
            if i < n - 1 {
                rl_0_cnt[i] += rl_0_cnt[i+1];
            }
        }
        
        let mut ans = rl_0_cnt[0];
        for i in 0..n {
            let mut tmp = 0;
            if i < n - 1 {
                tmp += lr_1_cnt[i] + rl_0_cnt[i+1];
            }
            else {
                tmp += lr_1_cnt[i];
            }
            ans = min(tmp, ans);
        }
        return ans
        
    }
}
