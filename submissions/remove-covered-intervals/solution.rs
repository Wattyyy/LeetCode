impl Solution {
    pub fn remove_covered_intervals(intervals: Vec<Vec<i32>>) -> i32 {
        let mut ans: Vec<Vec<i32>> = Vec::new();
        for i in 0..intervals.len() {
            let mut append = true;
            for j in 0..intervals.len() {
                if i == j {
                    continue;
                }
                let itv_0 = &intervals[i];
                let itv_1 = &intervals[j];
                if itv_1[0] <= itv_0[0] && itv_0[1] <= itv_1[1] {
                    append = false;
                }
            }
            if append {
                ans.push(intervals[i].clone());
            }
        }

        return ans.len() as i32;
    }
}


