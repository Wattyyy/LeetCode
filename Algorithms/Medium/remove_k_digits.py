# https://leetcode.com/problems/remove-k-digits/

from collections import deque
from bisect import bisect_right
class Solution:
    def removeKdigits(self, num, k):
        ls_num = list(map(int, list(num)))
        idx_stack, num_stack = [0], [ls_num[0]]
        rm_queue = deque([])
        for i, v in enumerate(ls_num):
            if i == 0:
                continue
            if num_stack[-1] <= v:
                idx_stack.append(i)
                num_stack.append(v)
            else:
                res = bisect_right(num_stack, v)
                cnt = len(num_stack) - res
                while cnt > 0:
                    idx, _ = idx_stack.pop(), num_stack.pop()
                    rm_queue.append(idx)
                    cnt -= 1
                idx_stack.append(i)
                num_stack.append(v)

        ans = []
        remain = k
        while 0 < remain and rm_queue:
            idx = rm_queue.popleft()
            ls_num[idx] = '-'    
            remain -= 1

        for _, v in enumerate(ls_num):
            if v == '-' or (len(ans) == 0 and v == 0):
                continue
            ans.append(v)
        
        while 0 < remain and ans:
            ans.pop()
            remain -= 1
            
        if not ans:
            return '0'
        return ''.join(list(map(str, ans)))

