# https://leetcode.com/problems/number-of-squareful-arrays

class Solution:
    def __init__(self):
        self.ans = 0

    def is_square(self, num):
        if num == 0 or num == 1:
            return True
        l, r = 1, num
        while l <= r:
            mid = (l + r) // 2
            if mid ** 2 == num:
                return True
            elif mid **2 < num:
                l = mid + 1
            else:
                r = mid - 1
        return False

    def backtrack(self, end, used, arr):
        N = len(arr)
        if used == 2 ** N - 1:
            self.ans += 1
            return
        next_num, next_idx = set(), []
        i = 0
        while i < N:
            val = (used >> i) & 1
            if (val == 0) and (arr[i] not in next_num) and (self.is_square(end + arr[i])):
                next_num.add(arr[i])
                next_idx.append(i)
            i += 1
        for idx in next_idx:
            used = used | 2 ** idx
            self.backtrack(arr[idx], used, arr)
            used = used ^ 2 ** idx
        
    def numSquarefulPerms(self, A):
        N = len(A)
        used = set()
        for i, v in enumerate(A):
            if v not in used:
                self.backtrack(v, 2 ** i, A)
                used.add(v)
        return self.ans
        
        
        