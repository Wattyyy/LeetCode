impl Solution {
    pub fn binary_search_left(nums: &Vec<i32>, target: &i32) -> usize {
        let mut idx = nums.len();
        let mut left = 0;
        let mut right = (nums.len() - 1) as i32;
        while left <= right {
            let mid = (left + right) / 2;
            if nums[mid as usize] < *target {
                left = mid + 1;
            } else if *target < nums[mid as usize] {
                right = mid - 1;
            } else {
                idx = mid as usize;
                right = mid - 1;
            }
        }
        return idx;
    }

    pub fn binary_search_right(nums: &Vec<i32>, target: &i32) -> usize {
        let mut idx = nums.len();
        let mut left = 0;
        let mut right = (nums.len() - 1) as i32;
        while left <= right {
            let mid = (left + right) / 2;
            if nums[mid as usize] < *target {
                left = mid + 1;
            } else if *target < nums[mid as usize] {
                right = mid - 1;
            } else {
                idx = mid as usize;
                left = mid + 1;
            }
        }
        return idx;
    }

    pub fn four_sum_count(
        nums1: Vec<i32>,
        nums2: Vec<i32>,
        nums3: Vec<i32>,
        nums4: Vec<i32>,
    ) -> i32 {
        let mut sum_12: Vec<i32> = Vec::new();
        let mut sum_34: Vec<i32> = Vec::new();

        for num1 in nums1.iter() {
            for num2 in nums2.iter() {
                sum_12.push(*num1 + *num2);
            }
        }
        sum_12.sort();

        for num3 in nums3.iter() {
            for num4 in nums4.iter() {
                sum_34.push(0 - *num3 - *num4);
            }
        }
        sum_34.sort();

        let mut ans = 0;
        for num in sum_12.iter() {
            let l_idx = Self::binary_search_left(&sum_34, num);
            let r_idx = Self::binary_search_right(&sum_34, num);
            if l_idx != sum_34.len() {
                ans += (r_idx - l_idx + 1) as i32;
            }
        }

        return ans;
    }
}


