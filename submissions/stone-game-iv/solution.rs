use std::collections::HashSet;

impl Solution {
    pub fn winner_square_game(n: i32) -> bool {
        let mut squares: HashSet<i32> = HashSet::new();
        for i in 1..((n + 1) as usize) {
            let v = (i * i) as i32;
            if v <= n {
                squares.insert(v);
            } else {
                break;
            }
        }

        let mut dp = vec![false; (n + 1) as usize];
        dp[0] = true;
        for i in 1..((n + 1) as usize) {
            if squares.contains(&(i as i32)) {
                dp[i] = true;
                continue;
            }
            let mut b = false;
            for j in 1..i {
                if j * j <= i {
                    b = b | dp[i - (j * j)];
                } else {
                    break;
                }
            }
            dp[i] = !b;
        }

        return dp[n as usize];
    }
}

