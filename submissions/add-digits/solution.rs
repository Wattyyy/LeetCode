impl Solution {
    pub fn add_digits(num: i32) -> i32 {
        let mut v = num.clone();
        while 10 <= v {
            let mut tmp = 0;
            while 0 < v {
                tmp += v % 10;
                v = v / 10;
            }
            v = tmp;
        }

        return v;
    }
}


