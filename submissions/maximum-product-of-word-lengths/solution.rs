// https://leetcode.com/problems/maximum-product-of-word-lengths

use std::collections::HashMap;
use std::cmp;

impl Solution {
    pub fn max_product(words: Vec<String>) -> i32 {
        let mut map: HashMap<String, u32> = HashMap::new();
        
        for word in words.iter(){
            let mut bit:u32 = 0;
            for c in word.chars(){
                let mut v = c as u32;
                v = u32::pow(2, v - 97);
                bit |= v;
            }
            map.insert(word.to_string(), bit);
        }
        
        let mut res:u32 = 0;
        let length = words.len();
        for l in 0..length{
            for r in l+1..length{
                let w1 = &words[l];
                let w2 = &words[r];
                let bit1 = map[w1];
                let bit2 = map[w2];
                if bit1 & bit2 == 0 {
                    res = cmp::max(res, (w1.len() as u32) * (w2.len() as u32));
                }
            }
        }
        res as i32
    }
}