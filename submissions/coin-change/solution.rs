use std::cmp::min;

impl Solution {
    pub fn coin_change(coins: Vec<i32>, amount: i32) -> i32 {
        let length = (amount + 1) as usize;
        let mut count = vec![10001; length];
        count[0] = 0;
        for coin in coins.iter() {
            let i = (*coin) as usize;
            if i < length {
                count[i] = 1;
            }
        }
        for i in 1..length {
            for coin in coins.iter() {
                let j = (*coin) as usize;
                if j < i {
                    count[i] = min(count[i - j] + 1, count[i]);
                }
            }
        }
        
        if count[length - 1] == 10001 {
            return -1;
        }
        return count[length - 1];
    }
}


