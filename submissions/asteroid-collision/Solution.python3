// https://leetcode.com/problems/asteroid-collision

class Solution:
    def asteroidCollision(self, asteroids):
        minus, plus = [], []
        for size in asteroids:
            if size < 0:
                broken = False
                while plus:
                    if plus[-1] < abs(size):
                        plus.pop()
                    elif plus[-1] == abs(size):
                        plus.pop()
                        broken = True
                        break
                    else:
                        broken = True
                        break
                if not broken:
                    minus.append(size)
            else:
                plus.append(size)
        ans = minus + plus
        return ans
            

            



        