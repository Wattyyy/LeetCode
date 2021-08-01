class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        if len(milestones) == 1:
            return 1
        arr = sorted(milestones)
        if arr[-1] - sum(arr[:-1]) < 2:
            return sum(arr)
        else:
            return sum(arr[:-1]) + sum(arr[:-1]) + 1
            
