impl Solution {
    pub fn search_insert(nums: Vec<i32>, target: i32) -> i32 {
        let mut left = 0;
        let mut right = (nums.len() - 1) as i32;
        let mut ans = 0;
        while left <= right {
            let mid = (left + right) / 2;
            if nums[mid as usize] == target {
                return mid as i32;
            } else {
                if nums[mid as usize] < target {
                    left = mid + 1;
                    ans = mid + 1;
                } else {
                    right = mid - 1;
                    ans = mid;
                }
            }
        }
        return ans;
    }
}


