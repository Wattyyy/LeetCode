impl Solution {
    pub fn detect_capital_use(word: String) -> bool {
        let arr = word.as_bytes();
        let mut cnt = 0;
        let mut is_capitalized = false;
        for i in 0..arr.len() {
            if i == 0 {
                is_capitalized = arr[i] <= 90;
            }
            cnt += (arr[i] <= 90) as i32;
        }

        if is_capitalized {
            return (cnt == arr.len() as i32) || (cnt == 1);
        } else {
            return cnt == 0;
        }
    }
}


