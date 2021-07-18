impl Solution {
    pub fn three_equal_parts(arr: Vec<i32>) -> Vec<i32> {
        let mut oneids: Vec<usize> = Vec::new();
        for i in 0..arr.len() {
            if arr[i] == 1 {
                oneids.push(i);
            }
        }
        
        let N = oneids.len();
        if N == 0 {
            return vec![0, 2]
        }
        if N % 3 != 0 {
            return vec![-1, -1]
        }
        
        let id1 = oneids[0];
        let id2 = oneids[N / 3 - 1];
        let id3 = oneids[N / 3];
        let id4 = oneids[2 * (N / 3) - 1];
        let id5 = oneids[2 * (N / 3)];
        let id6 = oneids[N - 1];
        
        if &arr[id1..=id2] != &arr[id3..=id4] || &arr[id3..=id4] != &arr[id5..=id6] {
            return vec![-1, -1]
        }
        
        let l1 = id3 - id2 - 1;
        let l2 = id5 - id4 - 1;
        let l3 = arr.len() - id6 - 1;
        if l3 > l1 || l3 > l2 {
            return vec![-1, -1]
        }
        let mut res = Vec::new();
        res.push((id2 + l3) as i32);
        res.push((id4 + l3 + 1) as i32);
        return res
        
    }
}
