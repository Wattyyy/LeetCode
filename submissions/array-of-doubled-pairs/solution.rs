use std::collections::HashMap;

impl Solution {
    pub fn can_reorder_doubled(mut arr: Vec<i32>) -> bool {
        arr.sort();
        let mut counter = HashMap::new();
        for num in arr.iter() {
            *counter.entry(num).or_insert(0) += 1;
        }

        for num in arr.iter() {
            if *counter.get(num).unwrap() == 0 {
                continue;
            }
            *counter.get_mut(num).unwrap() -= 1;

            let mut key = 0;

            if *num < 0 {
                if *num % 2 == 0 {
                    key += *num / 2;
                } else {
                    return false;
                }
            } else {
                key += *num * 2;
            }

            if let Some(v) = counter.get_mut(&key) {
                if 0 < *v {
                    *v -= 1;
                } else {
                    return false;
                }
            } else {
                return false;
            }
        }

        return true;
    }
}


