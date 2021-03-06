# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums):
        N = len(nums)
        if N==1:
            return nums
        L_products, R_products = [1 for _ in range(N)], [1 for _ in range(N)]
        L_products[0], R_products[N-1] = nums[0], nums[N-1] 
        for i in range(1, N):
            L_products[i] = L_products[i-1]*nums[i]
        for i in reversed(range(N-1)):
            R_products[i] = R_products[i+1]*nums[i]
        ans = [1 for _ in range(N)]
        ans[0], ans[N-1] = R_products[1], L_products[N-2]
        for i in range(1, N-1):
            ans[i] = L_products[i-1]*R_products[i+1]
        
        return ans
