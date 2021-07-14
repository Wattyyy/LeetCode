// https://leetcode.com/problems/reconstruct-original-digits-from-english

from collections import Counter
class Solution:
    def originalDigits(self, s: str) -> str:
        counter = Counter(list(s))
        ret = []
        evens = [['z', 'zero', '0'], ['w', 'two', '2'], ['u', 'four', '4'], ['x', 'six', '6'], ['g', 'eight', '8']]
        odds = [['o', 'one', '1'], ['t', 'three', '3'], ['f', 'five', '5'], ['s', 'seven', '7']]
        while counter:
            changed = False
            for item in evens:
                if item[0] in counter:
                    changed = True
                    for char in item[1]:
                        counter[char] -= 1
                        if counter[char] == 0:
                            del counter[char]
                    ret.append(item[2])
            if not changed:
                break
        
        while counter:
            changed = False
            for item in odds:
                if item[0] in counter:
                    changed = True
                    for char in item[1]:
                        counter[char] -= 1
                        if counter[char] == 0:
                            del counter[char]
                    ret.append(item[2])
            if not changed:
                break
        
        for _ in range(counter['i']):
            ret.append('9')
            
        ret = sorted(ret)
        return ''.join(ret)


        