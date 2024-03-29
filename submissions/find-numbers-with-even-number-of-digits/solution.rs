// https://leetcode.com/problems/find-numbers-with-even-number-of-digits

impl Solution {
    pub fn find_numbers(nums: Vec<i32>) -> i32 {
        let mut res:i32 = 0;
        for num in nums.iter() {
            if ((10 <= *num) & (*num < 100)) | ((1000 <= *num) & (*num < 10000)) | (*num == 100000){
                res += 1;
            }
        }
        res
        
    }
}