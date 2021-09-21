impl Solution {
    pub fn find_min(nums: Vec<i32>) -> i32 {
        let mut l = 0 as usize;
        let mut r = nums.len() - 1;
        while l < r {
            let mid = (l + r) / 2;
            if nums[l] <= nums[mid] && nums[mid] < nums[r] {
                return nums[l];
            }
            else if nums[l] >= nums[mid] && nums[mid] < nums[r] {
                r = mid;
                l = l + 1;
            }
            else {
                l = mid + 1;
            }
        }
        return nums[l];
        
    }
}
