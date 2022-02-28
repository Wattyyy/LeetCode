impl Solution {
    pub fn title_to_number(column_title: String) -> i32 {
        let arr = column_title.as_bytes();
        let mut ans = 0;
        for i in (0..arr.len()).rev() {
            let v = (arr[i] - b'@') as i32;
            ans += v * i32::pow(26, (arr.len() - i - 1) as u32);
        }
        return ans;
    }
}


