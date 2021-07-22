use std::cmp;

impl Solution {
    pub fn partition_disjoint(nums: Vec<i32>) -> i32 {
        let N = nums.len();
        let mut max_arr = vec![i32::MIN; N];
        let mut min_arr = vec![i32::MAX; N];
        
        for i in 0..N {
            if i == 0 {
                max_arr[0] = nums[0];
            }
            else {
                max_arr[i] = cmp::max(nums[i], max_arr[i-1]);
            }
        }
        
        for i in (0..N).rev() {
            if i == N - 1 {
                min_arr[N-1] = nums[N-1];
            }
            else {
                min_arr[i] = cmp::min(min_arr[i+1], nums[i]);
            }
        }
        
        let mut ans = i32::MAX;
        for i in 0..N {
            if i == N - 1 {
                break
            }
            else {
                if max_arr[i] <= min_arr[i+1] {
                    ans = cmp::min(ans, (i+1) as i32);
                }
            }
        }
        
        return ans
    }
}
