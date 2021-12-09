impl Solution {
    fn visit(i: i32, arr: &Vec<i32>, visited: &mut Vec<bool>) {
        visited[i as usize] = true;
        if arr[i as usize] == 0 {
            return;
        }

        let r_i = i - arr[i as usize];
        let l_i = i + arr[i as usize];
        if 0 <= r_i && !visited[r_i as usize] {
            Self::visit(r_i, arr, visited);
        }
        if l_i < (arr.len() as i32) && !visited[l_i as usize] {
            Self::visit(l_i, arr, visited);
        }

        return;
    }

    pub fn can_reach(arr: Vec<i32>, start: i32) -> bool {
        let mut visited: Vec<bool> = vec![false; arr.len()];
        Self::visit(start, &arr, &mut visited);
        for i in 0..visited.len() {
            if visited[i] && arr[i] == 0 {
                return true;
            }
        }

        return false;
    }
}




