impl Solution {
    pub fn num_decodings(s: String) -> i32 {
        let arr = s.as_bytes();
        if s.len() == 1 {
            let val = arr[0] - b'0';
            match val {
                0 => return 0,
                _ => return 1,
            }
        }

        let mut dp = vec![0; s.len()];
        if arr[0] - b'0' == 0 {
            return 0;
        }
        dp[0] = 1;

        if arr[1] - b'0' != 0 {
            dp[1] += 1;
        }
        if arr[0] - b'0' != 0 && (arr[0] - b'0') * 10 + arr[1] - b'0' <= 26 {
            dp[1] += 1;
        }

        for i in 2..s.len() {
            if arr[i] - b'0' != 0 {
                dp[i] += dp[i - 1];
            }
            if arr[i-1] - b'0' != 0 && (arr[i - 1] - b'0') * 10 + arr[i] - b'0' <= 26 {
                dp[i] += dp[i - 2];
            }
        }
        return dp[s.len() - 1];
    }
}


