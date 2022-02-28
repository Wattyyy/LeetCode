use std::collections::HashMap;

impl Solution {
    pub fn subarray_sum(nums: Vec<i32>, k: i32) -> i32 {
        let mut cum_sum = vec![0; nums.len()];
        for i in 0..cum_sum.len() {
            if i == 0 {
                cum_sum[i] = nums[i];
            } else {
                cum_sum[i] = nums[i] + cum_sum[i - 1];
            }
        }

        let mut counter: HashMap<i32, i32> = HashMap::new();
        counter.insert(0, 1);
        let mut ans = 0;
        for i in 0..cum_sum.len() {
            let key = cum_sum[i] - k;
            if counter.contains_key(&key) {
                ans += counter.get(&key).unwrap();
            }
            *counter.entry(cum_sum[i]).or_insert(0) += 1;
        }

        return ans;
    }
}


