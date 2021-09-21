use std::cmp::max;
impl Solution {
    pub fn find_max_consecutive_ones(nums: Vec<i32>) -> i32 {
        let mut cnt = 0;
        let mut ans = 0;
        for i in 0..nums.len() {
            if nums[i] == 1 {
                cnt += 1;
            }
            else {
                ans = max(cnt, ans);
                cnt = 0;
            }
        }
        ans = max(cnt, ans);
        return ans;
    }
}


