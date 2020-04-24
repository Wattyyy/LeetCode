# https://leetcode.com/problems/hand-of-straights/

from collections import OrderedDict
class Solution:
    def isNStraightHand(self, hand, W):
        if len(hand) % W != 0:
            return False
        od = OrderedDict()
        hand = sorted(hand)
        for _, val in enumerate(hand):
            if val not in od:
                od[val] = 0
            od[val] += 1
        arranged = []
        tmp = []
        while od:
            if not tmp:
                key =  next(iter(od))
                tmp.append(key)
                od[key] -= 1
            else:
                key = tmp[-1] + 1
                if key not in od: 
                    return False
                tmp.append(key)
                od[key] -= 1
            if od[key] == 0:
                del od[key]
            if len(tmp) == W:
                arranged.append(tmp)
                tmp = []
                
        return True

            
