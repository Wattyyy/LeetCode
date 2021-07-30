use std::collections::{HashMap, VecDeque};


impl Solution {
    pub fn min_jumps(arr: Vec<i32>) -> i32 {
        let N = arr.len();
        let mut val2ids: HashMap<i32, Vec<usize>> = HashMap::new();
        for i in (0..N).rev() {
            let key = arr[i];
            val2ids.entry(key).or_insert_with(Vec::new).push(i);
        }
        let mut queue: VecDeque<(usize, i32)> = VecDeque::with_capacity(N);
        queue.push_back((0, 0));
        let mut visited = vec![false; N];
        visited[0] = true;
       
        while 0 < queue.len() {
            let tp = queue.pop_front().unwrap();
            let idx = tp.0;
            let cnt = tp.1;
            if idx == N - 1 {
                return cnt
            }
            
            if 1 <= idx && !visited[idx-1] {
                queue.push_back((idx-1, cnt+1));
                visited[idx-1] = true;
            }
            if idx+1 < N && !visited[idx+1] {
                if idx+1 == N - 1 {
                    return cnt + 1
                }
                queue.push_back((idx+1, cnt+1));
                visited[idx+1] = true;
            }
            
            for next_id in &val2ids[&arr[idx]] {
                if !visited[*next_id] {
                    if *next_id == N - 1 {
                        return cnt + 1
                    }
                    queue.push_back((*next_id, cnt+1));
                    visited[*next_id] = true;
                }
            }
        }
        
        return -1
    }
}