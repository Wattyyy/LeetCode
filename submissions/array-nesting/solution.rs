use std::cmp::max;

impl Solution {
    pub fn dfs(idx: usize, cnt: i32, nums: &Vec<i32>, used: &mut Vec<bool>) -> i32 {
        let next_idx = nums[idx] as usize;
        if used[next_idx] {
            return cnt;
        } else {
            used[next_idx] = true;
            return Self::dfs(next_idx, cnt + 1, nums, used);
        }
    }

    pub fn array_nesting(nums: Vec<i32>) -> i32 {
        let mut used = vec![false; nums.len()];
        let mut ans = 1;
        for i in 0..nums.len() {
            let idx = nums[i] as usize;
            if used[idx] {
                continue;
            }
            used[idx] = true;
            let res = Self::dfs(idx, 1, &nums, &mut used);
            ans = max(res, ans);
        }
        return ans;
    }
}

