use std::cmp::{max, min};

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        if prices.len() == 0 {
            return 0;
        }
        let mut buy = prices[0];
        let mut ans = 0;
        for i in 0..prices.len() {
            if i == 0 {
                continue;
            }
            ans = max(ans, prices[i] - buy);
            buy = min(buy, prices[i]);
        }
        return ans;
    }
}


