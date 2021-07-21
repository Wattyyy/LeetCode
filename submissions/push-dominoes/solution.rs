impl Solution {
    pub fn push_dominoes(dominoes: String) -> String {
        let byte_arr = dominoes.as_bytes();
        let mut num_arr = vec![0; byte_arr.len()];
        let mut l_vec = Vec::new();
        let mut r_vec = Vec::new();
        for i in 0..byte_arr.len() {
            // char == 'L'        
            if byte_arr[i] == 76 {
                l_vec.push(i)
            }
            // char == 'R'
            if byte_arr[i] == 82 {
                r_vec.push(i)
            }
        }
        
        while 0 < l_vec.len() || 0 < r_vec.len() {
            for li in l_vec.iter() {
                num_arr[*li] -= 1;
            }
            for ri in r_vec.iter() {
                num_arr[*ri] += 1;
            }
            
            let mut new_l_vec = Vec::new();
            let mut new_r_vec = Vec::new();
            
            for li in l_vec.iter() {
                if 0 < *li && num_arr[*li-1] == 0 {
                    new_l_vec.push(*li-1);
                }
            }
            for ri in r_vec.iter() {
                if *ri+1 < num_arr.len() && num_arr[*ri+1] == 0 {
                    new_r_vec.push(*ri+1);
                }
            }
            
            l_vec = new_l_vec.clone();
            r_vec = new_r_vec.clone();
        }
        let mut res = String::new();
        for num in num_arr {
            match num {
                -1 => res.push('L'),
                1 => res.push('R'),
                _ => res.push('.')
            }
        }  
        return res
    }
}
