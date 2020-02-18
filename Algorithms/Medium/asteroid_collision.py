# https://leetcode.com/problems/asteroid-collision/

class Solution:
    def asteroidCollision(self, asteroids):
        if not asteroids:
            return []
        st, ans = [], []
        for i in range(len(asteroids)):
            ast = asteroids[i]
            if ast < 0:
                ans.append(ast)
            else:
                st.append(ast)
                break

        idx = i + 1
        while idx < len(asteroids):
            ast = asteroids[idx]
            if 0 < ast:
                st.append(ast)
                idx += 1
                continue
            else:
                if not st:
                    ans.append(ast)
                    idx += 1
                else:
                    while st:
                        if st[-1] > abs(ast):
                            idx += 1
                            break 
                        elif st[-1] == abs(ast):
                            st.pop()
                            idx += 1
                            break
                        else:
                            st.pop()
                            if not st:
                                ans.append(ast)
                                idx += 1
                                break

        ans.extend(st)
        return ans



