use std::collections::{BinaryHeap, HashMap};

impl Solution {
    pub fn network_delay_time(times: Vec<Vec<i32>>, n: i32, k: i32) -> i32 {
        let mut graph: HashMap<i32, Vec<(i32, i32)>> = HashMap::new();
        for i in 0..times.len() {
            let (u, v, w) = (times[i][0], times[i][1], times[i][2]);
            graph.entry(u).or_insert(vec![]).push((w, v));
        }

        let mut dist = vec![i32::MAX; (n + 1) as usize];
        dist[0] = 0;
        dist[k as usize] = 0;

        let mut min_heap: BinaryHeap<(i32, i32)> = BinaryHeap::new();
        min_heap.push((0, k));

        while let Some((d, u)) = min_heap.pop() {
            if dist[u as usize] < d {
                continue;
            }

            for (w, v) in graph.get(&u).unwrap_or(&vec![]) {
                if dist[*v as usize] > dist[u as usize] + w {
                    dist[*v as usize] = dist[u as usize] + w;
                    min_heap.push((dist[*v as usize], *v));
                }
            }
        }

        if dist.iter().any(|x| *x == i32::MAX) {
            return -1;
        }
        return *dist.iter().max().unwrap();
    }
}

