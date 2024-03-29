// https://leetcode.com/problems/find-peak-element

impl Solution {
    pub fn find_peak_element(nums: Vec<i32>) -> i32 {
        fn search(l: usize, r: usize, nums: Vec<i32>) -> usize {
            let mid = (l + r) / 2 as usize;
            if (mid == 0 || nums[mid-1] < nums[mid]) && (mid == nums.len()-1 || nums[mid] > nums[mid+1]) {
                return mid
            }
            else if (mid < nums.len()-1 && nums[mid] < nums[mid+1]) {
                return search(mid+1, r, nums)
            }
            else {
                return search(l, mid-1, nums)
            }
        }
        let res = search(0, nums.len()-1, nums) as i32;
        return res
    }
}