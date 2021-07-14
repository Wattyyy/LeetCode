// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string

impl Solution {
    pub fn remove_duplicates(s: String) -> String {
        let mut stack: Vec<char> = Vec::new();
        for c in s.chars() {
            let length = stack.len();
            if 0 < length && stack[length-1] == c {
                stack.pop();
            }
            else {
                stack.push(c);
            }
        }
        let res: String = stack.iter().collect();
        return res
    }
}
