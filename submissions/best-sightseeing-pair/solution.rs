use std::cmp::max;

impl Solution {
    pub fn max_score_sightseeing_pair(values: Vec<i32>) -> i32 {
        let mut cur_max = values[0] - 1;
        let mut ans = 0;
        for i in 1..values.len() {
            ans = max(cur_max + values[i], ans);
            cur_max = max(cur_max - 1, values[i] - 1);
        } 
        return ans;
    }
}
