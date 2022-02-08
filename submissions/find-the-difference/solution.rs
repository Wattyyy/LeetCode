impl Solution {
    pub fn find_the_difference(s: String, t: String) -> char {
        let mut s_counter = vec![0; 26];
        for num in s.as_bytes() {
            s_counter[(*num - b'a') as usize] += 1;
        }
        let mut t_counter = vec![0; 26];
        for num in t.as_bytes() {
            t_counter[(*num - b'a') as usize] += 1;
        }

        for i in 0..26 {
            if s_counter[i] != t_counter[i] {
                return (i as u8 + b'a') as char;
            }
        }

        return 'a';
    }
}


