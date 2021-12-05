# https://leetcode.com/problems/cinema-seat-allocation

from collections import defaultdict
class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        res = n * 2
        reserve_dict = defaultdict(list)
        for row, i in reservedSeats:
            reserve_dict[row].append(i)
        l_set = set([2, 3, 4, 5])
        c_set = set([4, 5, 6, 7])
        r_set = set([6, 7, 8, 9])
        for key in reserve_dict.keys():
            left, center, right = True, True, True
            for idx in reserve_dict[key]:
                if idx in l_set:
                    left = False
                if idx in c_set:
                    center = False
                if idx in r_set:
                    right = False
            
            if left and center and right:
                continue
            elif left and center:
                res -= 1
            elif center and right:
                res -= 1
            else:
                val = left + center + right
                if val == 1:
                    res -= 1
                elif val == 0:
                    res -= 2
            
        return res
                
                
