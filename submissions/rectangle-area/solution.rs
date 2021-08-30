impl Solution {
    pub fn compute_area(
        ax1: i32,
        ay1: i32,
        ax2: i32,
        ay2: i32,
        bx1: i32,
        by1: i32,
        bx2: i32,
        by2: i32,
    ) -> i32 {
        let total = (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1);
        if bx2 <= ax1 || ax2 <= bx1 || by2 <= ay1 || ay2 <= by1 {
            return total;
        }

        let length;
        // bx1 <= ax1 <= ax2 <= bx2
        if bx1 <= ax1 && ax1 <= ax2 && ax2 <= bx2 {
            length = ax2 - ax1;
        }
        // ax1 <= bx1 <= bx2 <= ax2
        else if ax1 <= bx1 && bx1 <= bx2 && bx2 <= ax2 {
            length = bx2 - bx1;
        }
        // ax1 <= bx1 <= ax2 <= bx2
        else if ax1 <= bx1 && bx1 <= ax2 && ax2 <= bx2 {
            length = ax2 - bx1;
        }
        // bx1 <= ax1 <= bx2 <= ax2
        else {
            length = bx2 - ax1;
        }

        let height;
        // by1 <= ay1 <= ay2 <= by2
        if by1 <= ay1 && ay1 <= ay2 && ay2 <= by2 {
            height = ay2 - ay1;
        }
        // ay1 <= by1 <= by2 <= ay2
        else if ay1 <= by1 && by1 <= by2 && by2 <= ay2 {
            height = by2 - by1;
        }
        // ay1 <= by1 <= ay2 <= by2
        else if ay1 <= by1 && by1 <= ay2 && ay2 <= by2 {
            height = ay2 - by1;
        }
        // by1 <= ay1 <= by2 <= ay2
        else {
            height = by2 - ay1;
        }

        return total - (height * length);
    }
}


