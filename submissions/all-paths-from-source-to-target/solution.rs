
impl Solution {
    pub fn back_track(
        node: i32,
        dst: i32,
        graph: &Vec<Vec<i32>>,
        path: &mut Vec<i32>,
        ans: &mut Vec<Vec<i32>>,
    ) {
        if node == dst {
            ans.push(path.clone());
            return;
        }
        for next in graph[node as usize].iter() {
            path.push(*next);
            Self::back_track(*next, dst, graph, path, ans);
            path.pop();
        }
        return;
    }
    pub fn all_paths_source_target(graph: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let dst = (graph.len() - 1) as i32;
        let mut path = vec![0];
        let mut ans: Vec<Vec<i32>> = Vec::new();
        Self::back_track(0, dst, &graph, &mut path, &mut ans);
        return ans;
    }
}


