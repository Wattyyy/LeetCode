use std::cmp::min;
impl Solution {
    pub fn min_eating_speed(piles: Vec<i32>, h: i32) -> i32 {
        let mut l = 1;
        let mut r = *piles.iter().max().unwrap();
        let mut ans = *piles.iter().max().unwrap();

        while l <= r {
            let mid = (l + r) / 2;
            let mut hour = 0;
            for v in piles.iter() {
                if *v % mid == 0 {
                    hour += *v / mid;
                } else {
                    hour += (*v / mid) + 1;
                }
            }
            if hour <= h {
                ans = min(ans, mid);
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }

        return ans;
    }
}


