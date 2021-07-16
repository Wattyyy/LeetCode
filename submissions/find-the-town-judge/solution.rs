use std::collections::HashMap;

impl Solution {
    pub fn find_judge(n: i32, trust: Vec<Vec<i32>>) -> i32 {
        let mut graph: HashMap<i32, Vec<i32>> = HashMap::new();
        for i in 0..trust.len() {
            let u = trust[i][0];
            let v = trust[i][1];
            graph.entry(u).or_insert(Vec::new()).push(v);
        }
        
        let mut judges = Vec::new();
        for i in 1..(n+1) {
            let key = i as i32;
            if !graph.contains_key(&key) {
                judges.push(key);
            }
        }
        
        for u in judges.iter() {
            let mut cnt = 0;
            for i in 0..trust.len() {
                if trust[i].iter().any(|&v| v == *u) {
                    cnt += 1;
                }
            }
            if cnt == n - 1 {
                return *u
            }
        }
        return -1
    }
}
