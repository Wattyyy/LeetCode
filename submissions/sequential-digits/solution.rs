impl Solution {
    pub fn sequential_digits(low: i32, high: i32) -> Vec<i32> {
        let mut nums: Vec<i32> = Vec::new();
        for i in 1..10 {
            nums.push(i as i32);
            for j in (i + 1)..10 {
                let val = nums[nums.len() - 1] * 10 + (j as i32);
                nums.push(val);
            }
        }

        let mut ans: Vec<i32> = Vec::new();
        for i in 0..nums.len() {
            if low <= nums[i] && nums[i] <= high {
                ans.push(nums[i]);
            }
        }
        ans.sort();
        return ans;
    }
}


