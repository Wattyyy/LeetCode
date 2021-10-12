use std::collections::VecDeque;

impl Solution {
    pub fn topological_sort(length: usize, graph: &Vec<Vec<usize>>) -> Vec<usize> {
        let mut indegree = vec![0; length];
        let mut queue = VecDeque::new();
        for i in 0..length {
            for j in graph[i].iter() {
                indegree[*j] += 1;
            }
        }
        for i in 0..length {
            if indegree[i] == 0 {
                queue.push_back(i);
            }
        }

        let mut res = Vec::new();
        while 0 < queue.len() {
            let u = queue.pop_front().unwrap();
            res.push(u);
            for v in graph[u].iter() {
                indegree[*v] -= 1;
                if indegree[*v] == 0 {
                    queue.push_back(*v)
                }
            }
        }
        return res;
    }

    pub fn find_longest_chain(pairs: Vec<Vec<i32>>) -> i32 {
        let length = pairs.len();
        let mut graph: Vec<Vec<usize>> = vec![vec![]; length];
        let mut count = vec![0; length];
        for u in 0..length {
            for v in 0..length {
                if u == v {
                    continue;
                }
                if pairs[u][1] < pairs[v][0] {
                    graph[u].push(v);
                }
            }
        }

        let order = Self::topological_sort(length, &graph);
        for u in order.iter() {
            if count[*u] != 0 {
                continue;
            }
            count[*u] = 1;
            let mut queue = VecDeque::new();
            queue.push_back(*u);
            while 0 < queue.len() {
                let src = queue.pop_front().unwrap();
                let prev = count[src];
                for dist in graph[src].iter() {
                    if count[*dist] < prev + 1 {
                        count[*dist] = prev + 1;
                        queue.push_back(*dist);
                    }
                }
            }
        }

        return *count.iter().max().unwrap();
    }
}


