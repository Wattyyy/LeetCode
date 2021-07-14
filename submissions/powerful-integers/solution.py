// https://leetcode.com/problems/powerful-integers

from typing import List
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        st = set()
        if x == 1 and y == 1:
            if 2 <= bound:
                return [2]
            else:
                return []
        elif x == 1:
            i = 0
            while (pow(y, i) + 1 <= bound):
                st.add(pow(y, i) + 1)
                i += 1
            return list(st)
        elif y == 1:
            i = 0
            while (pow(x, i) + 1 <= bound):
                st.add(pow(x, i) + 1)
                i += 1
            return list(st)
        else:
            for i in range(21):
                for j in range(21):
                    val = pow(x, i) + pow(y, j)
                    if val <= bound:
                        st.add(val)
            return list(st)

            
        

