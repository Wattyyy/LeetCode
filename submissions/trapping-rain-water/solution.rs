impl Solution {
    pub fn trap(height: Vec<i32>) -> i32 {
        let N = height.len();
        if N == 0 {
            return 0
        }
        
        let mut water = vec![0; N];
        let mut l_idx = 0;
        let mut st = 0;
        let mut l_height = 0;
        
        
        for i in 0..N {
            if 0 < height[i] {
                l_idx = i;
                st = i;
                l_height = height[i];
                break
            }
        }
        
        for i in (st+1)..N {
            if l_height > height[i] {
                water[i] = l_height - height[i];
            }
            else {
                l_idx = i;
                l_height = height[i];
            }
        }
        
        let mut r_idx = N - 1;
        let mut r_height = height[N-1];
        for i in ((l_idx+1)..N).rev() {
            if height[i] < r_height {
                water[i] = r_height - height[i];
            }
            else {
                water[i] = 0;
                r_idx = i;
                r_height = height[i];
            }
        }
        return water.iter().sum()
        
    }
}
