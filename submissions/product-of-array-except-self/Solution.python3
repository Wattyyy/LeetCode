// https://leetcode.com/problems/product-of-array-except-self

class Solution:
    def productExceptSelf(self, nums):
        N = len(nums)
        L, R = [0] * N, [0] * N
        output = [0] * N
        for i in range(N):
            if i == 0:
                L[i] = nums[i]
            else:
                L[i] = L[i - 1] * nums[i]
        for i in reversed(range(N)):
            if i == N - 1:
                R[i] = nums[i]
            else:
                R[i] = R[i + 1] * nums[i]
        for i in range(N):
            if i == 0:
                output[i] = R[i + 1]
            elif i == N - 1:
                output[i] = L[i - 1]
            else:
                output[i] = L[i - 1] * R[i + 1]
        return output
            
        
        