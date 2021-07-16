use std::collections::VecDeque;

impl Solution {
    pub fn can_finish(num_courses: i32, prerequisites: Vec<Vec<i32>>) -> bool {
        let N = num_courses as usize;
        let mut graph = vec![vec![]; N];
        let mut indegree = vec![0; N];
        let mut queue = VecDeque::new();
        
        for i in 0..prerequisites.len() {
            let u = prerequisites[i][1];
            let v = prerequisites[i][0];
            graph[u as usize].push(v);
            indegree[v as usize] += 1;
        }
        
        let mut cnt = 0;
        for u in 0..N {
            if indegree[u] == 0 {
                queue.push_back(u as i32);
                cnt += 1;
            }
        }
        
        while 0 < queue.len() {
            let u = queue.pop_front().unwrap();
            for v in graph[u as usize].iter() {
                indegree[*v as usize] -= 1;
                if indegree[*v as usize] == 0 {
                    queue.push_back(*v);
                    cnt += 1;
                }
            }
        }
        
        return cnt == num_courses
        
    }
}
