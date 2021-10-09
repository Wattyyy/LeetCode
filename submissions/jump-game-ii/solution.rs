use std::cmp::min;

impl Solution {
    pub fn jump(nums: Vec<i32>) -> i32 {
        let mut dp = vec![10000; nums.len()];
        dp[0] = 0;
        for i in 0..nums.len() {
            let step = nums[i] as usize;
            for j in i..(i + step + 1) {
                if nums.len() <= j {
                    break;
                } else {
                    dp[j] = min(dp[j], dp[i] + 1);
                }
            }
        }

        return dp[nums.len() - 1];
    }
}
