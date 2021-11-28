use std::cmp::min;

impl Solution {
    pub fn bisect_right(arr: &Vec<usize>, val: usize) -> usize {
        let mut left = 0;
        let mut right = arr.len() - 1;
        let mut res = arr.len();
        while left <= right {
            let mid = (left + right) / 2;
            if val < arr[mid] {
                res = min(res, mid);
                // avoid overflow
                if mid == 0 {
                    return res;
                }
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return res;
    }

    pub fn daily_temperatures(temperatures: Vec<i32>) -> Vec<i32> {
        let length = temperatures.len();
        let mut ans: Vec<i32> = vec![0; length];
        let mut tmp2idx = vec![Vec::new(); 101];

        for i in 0..length {
            tmp2idx[temperatures[i] as usize].push(i);
        }

        for l_idx in 0..length {
            let base_temp = temperatures[l_idx] as usize;
            let mut r_idx = length;
            for t in base_temp + 1..101 {
                if 0 < tmp2idx[t].len() {
                    let res = Self::bisect_right(&tmp2idx[t], l_idx);
                    if res < tmp2idx[t].len() {
                        r_idx = min(r_idx, tmp2idx[t][res])
                    }
                }
            }
            if r_idx != length {
                ans[l_idx] = (r_idx - l_idx) as i32;
            }
        }

        return ans;
    }
}


