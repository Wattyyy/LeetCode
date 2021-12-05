# https://leetcode.com/problems/bulls-and-cows


class Solution:
    def getHint(self, secret, guess):
        s_used, g_used = set(), set()
        bull = 0
        for idx, (s_char, g_char) in enumerate(zip(secret, guess)):
            if s_char == g_char:
                bull += 1
                s_used.add(idx)
                g_used.add(idx)

        print(s_used)
        print(g_used)

        cow = 0
        for i, s_char in enumerate(secret):
            for j, g_char in enumerate(guess):
                if (s_char == g_char) and (i not in s_used) and (j not in g_used):
                    cow += 1
                    s_used.add(i)
                    g_used.add(j)

        print(s_used)
        print(g_used)

        return "{}A{}B".format(bull, cow)
