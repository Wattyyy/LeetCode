use std::cmp::max;
impl Solution {
    pub fn length_of_lis(nums: Vec<i32>) -> i32 {
        let mut arr = vec![i32::MAX; nums.len()];
        let mut ans = 0;
        for num in nums.iter() {
            if let Err(i) = arr.binary_search(num) {
                arr[i] = *num;
                ans = max(ans, (i + 1) as i32);
            }
        }
        return ans;
    }
}
