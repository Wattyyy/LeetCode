# https://leetcode.com/problems/reverse-bits


class Solution:
    def reverseBits(self, n):
        binary = list(bin(n)[2:])[::-1]
        p = 31
        while 0 <= p:
            if n < 2 ** p:
                binary.append(str(0))
                p -= 1
            else:
                break
        return int("".join(binary), 2)

        # return int(','.join(binary), 2)
