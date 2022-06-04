impl Solution {
    pub fn min_remove_to_make_valid(s: String) -> String {
        let mut stack: Vec<(usize, char)> = Vec::new();
        for (i, c) in s.chars().enumerate() {
            if c != '(' && c != ')' {
                continue;
            }
            if stack.len() == 0 {
                stack.push((i, c));
                continue;
            }
            let top = stack[stack.len() - 1].1;
            if top == '(' && c == ')' {
                stack.pop();
            } else {
                stack.push((i, c));
            }
        }
        let mut remove = vec![false; s.len()];
        for item in stack.iter() {
            remove[item.0] = true;
        }
        let mut ans: Vec<char> = Vec::new();
        for (i, c) in s.chars().enumerate() {
            if !remove[i] {
                ans.push(c);
            }
        }

        return ans.iter().collect();
    }
}


