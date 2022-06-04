impl Solution {
    fn push_to_stack(s: &String, stack: &mut Vec<char>) {
        for c in s.chars() {
            if c == '#' {
                if stack.len() > 0 {
                    stack.pop();
                }
            } else {
                stack.push(c);
            }
        }
        return;
    }

    pub fn backspace_compare(s: String, t: String) -> bool {
        let mut s_stack: Vec<char> = Vec::new();
        let mut t_stack: Vec<char> = Vec::new();
        Solution::push_to_stack(&s, &mut s_stack);
        Solution::push_to_stack(&t, &mut t_stack);
        if s_stack.len() != t_stack.len() {
            return false;
        }
        for i in 0..s_stack.len() {
            if s_stack[i] != t_stack[i] {
                return false;
            }
        }
        return true;
    }
}

