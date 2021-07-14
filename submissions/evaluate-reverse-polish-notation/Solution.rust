// https://leetcode.com/problems/evaluate-reverse-polish-notation

use std::collections::HashSet;
impl Solution {
    pub fn eval_rpn(tokens: Vec<String>) -> i32 {
        let mut vec = Vec::new();
        let mut operators: HashSet<String> = ["+", "-", "*", "/"].iter().map(|&ope| ope.to_owned()).collect();
        for v in tokens.iter(){
            if !operators.contains(v){
                let val:i32 = v.parse().unwrap();
                vec.push(val);
            }
            else {
                let num2 = vec.pop().unwrap();
                let num1 = vec.pop().unwrap();
                if v == "+" {
                    vec.push(num1 + num2);
                }
                else if v == "-" {
                    vec.push(num1 - num2);
                }
                else if v == "*" {
                    vec.push(num1 * num2);
                }
                else {
                    vec.push(num1 / num2);
                }
            }
        }
    return vec[0]
    }
}