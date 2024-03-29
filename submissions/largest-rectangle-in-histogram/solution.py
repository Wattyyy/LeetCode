# https://leetcode.com/problems/largest-rectangle-in-histogram


class Solution:
    def largestRectangleArea(self, heights):
        if not heights:
            return 0
        st = [0]
        idx = 1
        ans = 0
        while idx < len(heights):
            while heights[idx] < heights[st[-1]]:
                if len(st) == 1:
                    l_idx = st.pop(-1)
                    ans = max(ans, idx * heights[l_idx])
                    break
                l_idx = st.pop(-1)
                ans = max(ans, (idx - (st[-1] + 1)) * heights[l_idx])

            st.append(idx)
            idx += 1

        while 1 < len(st):
            l_idx = st.pop(-1)
            ans = max(ans, (len(heights) - (st[-1] + 1)) * heights[l_idx])
        ans = max(ans, heights[st[0]] * len(heights))
        return ans
