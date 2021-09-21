impl Solution {
    pub fn number_of_arithmetic_slices(nums: Vec<i32>) -> i32 {
        if nums.len() < 3 {
            return 0;
        }
        let mut ans = 0;
        let mut diff = nums[1] - nums[0];
        let mut cnt = 2;
        for i in 2..nums.len() {
            let tmp = nums[i] - nums[i-1];
            if diff == tmp {
                cnt += 1;
            }
            else {
                diff = tmp;
                ans += (cnt - 2) * (cnt - 1) / 2;
                cnt = 2;
            }
        }
        ans += (cnt - 2) * (cnt - 1) / 2;
        return ans;
        
    }
}
