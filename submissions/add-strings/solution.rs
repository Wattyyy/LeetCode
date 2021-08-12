use std::str;

impl Solution {
    pub fn add_strings(num1: String, num2: String) -> String {
        let mut v1 = num1.as_bytes().to_vec();
        let mut v2 = num2.as_bytes().to_vec();
        v1.reverse();
        v2.reverse();
        
        if v1.len() < v2.len() {
            while v1.len() < v2.len() {
                v1.push(48);
            }
        }
        else {
            while v2.len() < v1.len() {
                v2.push(48);
            }
        }
        
        let mut carry = 0;
        let mut ans = Vec::new();
        for i in 0..v1.len() {
            let val = (v1[i] - 48) + (v2[i] - 48) + carry;
            if 10 <= val {
                carry = 1;
            }
            else {
                carry = 0;
            }
            ans.push(val % 10 + 48);
        }
        if carry == 1 {
            ans.push(1 + 48)
        }
        ans.reverse();
        
        return String::from(str::from_utf8(&ans).unwrap());
        
    }
}
