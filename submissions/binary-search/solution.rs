impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let r = nums.binary_search(&target);
        match r {
            Ok(v) => v as i32,
            Err(_) => -1,
        }
    }
}


