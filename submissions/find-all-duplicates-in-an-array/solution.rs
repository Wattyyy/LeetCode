impl Solution {
    pub fn find_duplicates(mut nums: Vec<i32>) -> Vec<i32> {
        let length = nums.len();
        let mut ans: Vec<i32> = Vec::new();
        for i in 0..length {
            let idx = ((nums[i]).abs() - 1) as usize;
            if nums[idx] < 0 {
                ans.push((nums[i]).abs());
            }
            else {
                nums[idx] = nums[idx] * (-1);
            }
        }
        return ans;
    }
}


