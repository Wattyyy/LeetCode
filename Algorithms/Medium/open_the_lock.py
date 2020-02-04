# https://leetcode.com/problems/open-the-lock/

from collections import defaultdict, deque
class Solution:
    def calc(self, string, i, j):
        int_ls = list(map(int, string))
        int_ls[i] += j
        if int_ls[i] == 10:
            int_ls[i] = 0
        if int_ls[i] == -1:
            int_ls[i] = 9
        str_ls = [str(num) for num in  int_ls]
        return "".join(str_ls)
             
        
    def openLock(self, deadends, target):
        deadends = set(deadends)
        count_dict = defaultdict(int)
        count_dict["0000"], count_dict[target] = 0, 0
        if "0000" in deadends:
            return -1
        
        q = deque(["0000"])
        nums = [-1, 1]
        while q:
            string = q.popleft()
            if string == target:
                return count_dict[string]
            for i in range(4):
                for num in nums:
                    res = self.calc(string, i, num)
                    if (res not in deadends) and (count_dict[res] == 0) and (res != "0000"):
                        q.append(res)
                        count_dict[res] = count_dict[string] + 1

        return -1
        
