impl Solution {
    pub fn champagne_tower(poured: i32, query_row: i32, query_glass: i32) -> f64 {
        let length = (query_row + 1) as usize;
        let mut amount: Vec<Vec<f64>> = vec![vec![0 as f64; length]; length];
        let mut excess: Vec<Vec<f64>> = vec![vec![0 as f64; length]; length];
        amount[0][0] = (poured as f64).min(1.0);
        excess[0][0] = ((poured - 1) as f64).max(0.0);
        
        for r in 1..length {
            for c in 0..(r + 1) {
                let mut p = 0.0;
                if c == 0 {
                    p = excess[r - 1][c] / 2.0;
                } else if c == r {
                    p = excess[r - 1][c - 1] / 2.0;
                } else {
                    p = (excess[r - 1][c - 1] / 2.0) + (excess[r - 1][c] / 2.0);
                }
                amount[r][c] = p.min(1.0);
                excess[r][c] = (p - 1.0).max(0.0);
            }
        }

        return amount[query_row as usize][query_glass as usize];
    }
}


