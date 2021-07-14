// https://leetcode.com/problems/sliding-window-maximum

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums:
            return []
        val_deque = deque([])
        idx_deque = deque([])
        ans = [0] * (len(nums) - k + 1)
        for i in range(k):
            if (len(val_deque) == 0) or (val_deque[-1] >= nums[i]):
                val_deque.append(nums[i])
                idx_deque.append(i)
            else:
                while val_deque and val_deque[-1] < nums[i]:
                    val_deque.pop()
                    idx_deque.pop()
                val_deque.append(nums[i])
                idx_deque.append(i)
                
        for i in range(k, len(nums)):
            if (len(val_deque) == k) or (idx_deque[0] == i - k):    
                val = val_deque.popleft()
                idx_deque.popleft()
            else:
                val = val_deque[0]    
            ans[i-k] = val
            
            if len(val_deque) == 0 or (val_deque[-1] >= nums[i]):
                val_deque.append(nums[i])
                idx_deque.append(i)
            else:
                while val_deque and val_deque[-1] < nums[i]:
                    val_deque.pop()
                    idx_deque.pop()
                val_deque.append(nums[i])
                idx_deque.append(i)
                
        ans[-1] = val_deque[0]
        return ans
                
            
            

        
        