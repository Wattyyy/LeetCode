impl Solution {
    pub fn three_sum_multi(arr: Vec<i32>, target: i32) -> i32 {
        let mut counter = vec![0; 101];
        for i in 0..arr.len() {
            counter[arr[i] as usize] += 1;
        }
        
        let M = 1000000007;
        let mut ans = 0;
        for i in 0..arr.len() {
            counter[arr[i] as usize] -= 1;
            for j in (i+1)..arr.len() {
                counter[arr[j] as usize] -= 1;
                let val = target - arr[i] - arr[j];
                if 0 <= val && val <= 100 {
                    ans += counter[val as usize];
                    ans = ans % M;
                }
            }
            for j in (i+1)..arr.len() {
                counter[arr[j] as usize] += 1;
            }
        }
        
        ans
    }
}
