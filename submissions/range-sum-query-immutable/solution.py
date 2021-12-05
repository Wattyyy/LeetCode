# https://leetcode.com/problems/range-sum-query-immutable

class NumArray:
    
    def __init__(self, nums):
        self.length = len(nums)
        self.tree = [0 for _ in range(2*self.length)]
        # build tree 
        n = self.length
        i = n
        j = 0
        # fill in elements of n~2n-1
        while i<2*n:
            self.tree[i] = nums[j]
            i += 1
            j += 1
        # fill in elements of 1~n-1
        for i in range(n-1, 0, -1):
            self.tree[i] = self.tree[i*2] + self.tree[i*2 + 1]
        
    def sumRange(self, l, r):
        if l > r:
            l, r = r, l
        # 0 <= l,r < n
        n = self.length
        l += n
        r += n
        res = 0
        while l<=r:
            
            if l%2==1:
                res += self.tree[l]
                l += 1
            if r%2==0:
                res += self.tree[r]
                r -= 1
            l //= 2
            r //= 2
        return res
       




# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)