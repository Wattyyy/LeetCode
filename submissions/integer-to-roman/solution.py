# https://leetcode.com/problems/integer-to-roman

class Solution:
    def intToRoman(self, num: int) -> str:
        divs = [1000, 100, 10, 1]
        div2symbols = {1000: ['M', 'M', 'M'], 100: ['M', 'D', 'C'], 10: ['C', 'L', 'X'], 1: ['X', 'V', 'I']}
        output = []
        for d in divs:
            q = num // d
            o_symbol = div2symbols[d][2]
            f_symbol = div2symbols[d][1]
            t_symbol = div2symbols[d][0]
            if 1 <= q <= 3:
                output.append(o_symbol * q)
            elif q == 4:
                output.append(o_symbol + f_symbol)
            elif 5 <= q <= 8:
                output.append(f_symbol + (o_symbol) * (q - 5))
            elif q == 9:
                output.append(o_symbol + t_symbol)
            num = num % d

        return ''.join(output)

                



        


        