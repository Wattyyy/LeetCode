// https://leetcode.com/problems/reordered-power-of-2

class Solution:
    def reorderedPowerOf2(self, N):
        num = 2 
        st = set()
        st.add(tuple(['1']))
        while num <= 10 ** 9:
            tp = tuple(sorted(list(str(num))))
            st.add(tp)
            num *= 2
        if tuple(sorted(list(str(N)))) in st:
            return True
        return False
        





        
        