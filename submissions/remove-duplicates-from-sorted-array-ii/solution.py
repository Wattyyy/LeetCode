from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # search index
        idx = -1
        prev_num = -100000
        cnt = 0
        for i, num in enumerate(nums):
            if num == prev_num:
                cnt += 1
                if 3 <= cnt:
                    idx = i
                    break
            else:
                prev_num = num
                cnt = 1

        if idx == -1:
            return len(nums)

        # replace nums
        prev_num = -100000
        cnt = 0
        N = len(nums)
        for i in range(N):
            num = nums[i]
            if num == prev_num:
                cnt += 1
            else:
                prev_num = num
                cnt = 1

            if 3 <= cnt:
                continue

            if idx < i:
                nums[idx] = num
                idx += 1

        return idx


