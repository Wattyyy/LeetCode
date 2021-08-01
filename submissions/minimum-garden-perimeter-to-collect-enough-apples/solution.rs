impl Solution {
    pub fn minimum_perimeter(needed_apples: i64) -> i64 {
        let N = 100000 as usize;
        let mut arr: Vec<i64> = vec![0; N+1];
        arr[1] = 12;
        for n in 2..(N+1) {
            let v = n as i64;
            let S = (3 * v * v + v) / 2;
            arr[n] = 8 * S - 4 * v;
        }
        for n in 1..(N+1) {
            arr[n] += arr[n-1];
        }
        for n in 1..(N+1) {
            if needed_apples <= arr[n] {
                return (n as i64) * 8
            }
        }
        return 0
    }
}
