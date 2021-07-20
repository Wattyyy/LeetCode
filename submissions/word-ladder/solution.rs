use std::collections::HashMap;
use std::collections::VecDeque;
use std::collections::HashSet;

impl Solution {
    pub fn ladder_length(begin_word: String, end_word: String, word_list: Vec<String>) -> i32 {
        let mut graph: HashMap<String, Vec<String>> = HashMap::new();
        graph.insert(begin_word.clone(), Vec::new());
        
        let mut wl1 = word_list.clone();
        wl1.push(begin_word.clone());

        for word1 in wl1 {
            graph.insert(word1.clone(), Vec::new());
            let s1 = word1.as_bytes();
            for word2 in word_list.iter() {
                let mut diff = 0;
                let s2 = word2.as_bytes();
                for i in 0..word1.len() {
                    if s1[i] != s2[i] {
                        diff += 1;
                    }
                }
                if diff == 1 {
                    graph.get_mut(&word1).unwrap().push(word2.clone());
                }
            }
            // println!("{:?}", graph[&word1]);
        }
    
        if !graph.contains_key(&end_word) {
            return 0
        }

        let mut ans = 0;
        let mut used = HashSet::new();
        let mut queue: VecDeque<(String, i32)> = VecDeque::with_capacity(word_list.len() + 2);
        queue.push_back((begin_word.clone(), 1));
        used.insert(begin_word.clone());
        while 0 < queue.len() {
            let tp = queue.pop_front().unwrap();
            if tp.0 == end_word {
                ans = tp.1;
                break
            }
            for next in &graph[&tp.0] {
                if !used.contains(next) {
                    queue.push_back((next.clone(), tp.1 + 1));
                    used.insert(next.clone());
                }
            }
        }

        return ans 
    }
}
