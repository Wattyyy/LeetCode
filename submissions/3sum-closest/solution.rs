impl Solution {
    pub fn three_sum_closest(nums: Vec<i32>, target: i32) -> i32 {
        let mut diff = i32::MAX;
        let mut ans = 0;
        let mut arr = nums.clone();
        arr.sort();
        for i in 0..arr.len()-2 {
            let mut p1 = i + 1;
            let mut p2 = arr.len() - 1;
            while p1 < p2 {
                let val = arr[i] + arr[p1] + arr[p2];
                if (val - target).abs() < diff {
                    diff = (val - target).abs();
                    ans = val;
                    
                }
                if target < val {
                    p2 -= 1;
                }
                else {
                    p1 += 1;
                }
            }   
        }
        return ans
    }
}
