# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold


class NumArray:
    def __init__(self, nums):
        if len(nums) > 0:
            self.length = len(nums)
            self.tree = [0 for _ in range(2 * self.length)]

            # build tree
            n = self.length
            i = n
            j = 0
            while i < 2 * n:
                self.tree[i] = nums[j]
                i += 1
                j += 1
            for i in range(n - 1, 0, -1):
                self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def update(self, pos, val):
        # 0 <= pos < n
        n = self.length
        pos += n
        self.tree[pos] = val
        while pos > 0:
            left = pos
            right = pos
            if pos % 2 == 0:
                right = pos + 1
            else:
                left = pos - 1
            self.tree[pos // 2] = self.tree[left] + self.tree[right]
            pos //= 2

    def sumRange(self, l, r):
        if l > r:
            l, r = r, l
        # 0 <= l,r < n
        n = self.length
        l += n
        r += n
        res = 0
        while l <= r:
            # check l is right child
            if l % 2 == 1:
                res += self.tree[l]
                l += 1
            # check r is left child
            if r % 2 == 0:
                res += self.tree[r]
                r -= 1
            l //= 2
            r //= 2
        return res


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold):
        N = len(arr)
        seg_tree = NumArray(arr)
        ans = 0
        for i in range(N):
            if i + k - 1 > N - 1:
                break
            avg = (seg_tree.sumRange(i, i + k - 1)) / k
            if threshold <= avg:
                ans += 1
        return ans
