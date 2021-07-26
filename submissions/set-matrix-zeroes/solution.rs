impl Solution {
    pub fn set_zeroes(matrix: &mut Vec<Vec<i32>>) {
        let R = matrix.len();
        let C = matrix[0].len();
        let mut r0_flag = false;
        let mut c0_flag = false;
        
        if matrix[0][0] == 0 {
            r0_flag = true;
            c0_flag = true;
        }
        for r in 1..R {
            if matrix[r][0] == 0 {
                c0_flag = true;
                break
            }
        }
        for c in 1..C {
            if matrix[0][c] == 0 {
                r0_flag = true;
                break
            }
        }
        
        for r in 1..R {
            for c in 1..C {
                if matrix[r][c] == 0 {
                    matrix[0][c] = 0;
                    matrix[r][0] = 0;
                }
            }
        }
        
        for c in 1..C {
            if matrix[0][c] == 0 {
                for r in 0..R {
                    matrix[r][c] = 0;
                }
            }
        }
        for r in 1..R {
            if matrix[r][0] == 0 {
                for c in 0..C {
                    matrix[r][c] = 0;
                }
            }
        }
        
        if r0_flag {
            for c in 0..C {
                matrix[0][c] = 0;
            }
        }
        if c0_flag {
            for r in 0..R {
                matrix[r][0] = 0;
            }
        }
        
    }
}
