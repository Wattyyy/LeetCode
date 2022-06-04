use std::cmp::min;

impl Solution {
    pub fn min_domino_rotations(tops: Vec<i32>, bottoms: Vec<i32>) -> i32 {
        let mut tops_ans = i32::MAX;
        for n in 1..7 {
            let num = n as i32;
            let mut cnt = 0;
            for i in 0..tops.len() {
                if tops[i] == num {
                    continue;
                } else if bottoms[i] == num {
                    cnt += 1;
                } else {
                    cnt = i32::MAX;
                    break;
                }
            }
            tops_ans = min(tops_ans, cnt);
        }

        let mut bottoms_ans = i32::MAX;
        for n in 1..7 {
            let num = n as i32;
            let mut cnt = 0;
            for i in 0..tops.len() {
                if bottoms[i] == num {
                    continue;
                } else if tops[i] == num {
                    cnt += 1;
                } else {
                    cnt = i32::MAX;
                    break;
                }
            }
            bottoms_ans = min(bottoms_ans, cnt);
        }

        let ans = min(tops_ans, bottoms_ans);
        if ans == i32::MAX {
            return -1;
        }
        return ans;
    }
}


