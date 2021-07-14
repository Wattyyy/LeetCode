// https://leetcode.com/problems/daily-temperatures

from collections import deque
class Solution:
    def dailyTemperatures(self, T):
        if not T:
            return []
        N = len(T)
        ans = [0]*N
        st = deque( [(T[0], 0)] )
        for i in range(1, N):
            if st[-1][0]>=T[i]:
                st.append( (T[i], i) )
            else:
                while st:
                    top_val, top_idx = st[-1][0], st[-1][1]
                    if top_val < T[i]:
                        ans[top_idx] = i - top_idx
                        st.pop()
                    else:
                        break
                st.append( (T[i], i) )
                        
        return ans