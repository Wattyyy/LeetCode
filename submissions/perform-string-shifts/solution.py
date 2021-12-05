# https://leetcode.com/problems/perform-string-shifts

from collections import deque


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        deq = deque(list(s))
        for d, n in shift:
            cnt = 0
            if d == 0:
                while cnt < n:
                    tmp = deq.popleft()
                    deq.append(tmp)
                    cnt += 1
            else:
                while cnt < n:
                    tmp = deq.pop()
                    deq.appendleft(tmp)
                    cnt += 1
        deq = list(deq)
        return "".join(deq)
