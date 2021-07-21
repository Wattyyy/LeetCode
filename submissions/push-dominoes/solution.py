class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        N = len(dominoes)
        arr = [0] * N
        l_ids, r_ids = [], []
        for i, char in enumerate(dominoes):
            if char == 'L':
                l_ids.append(i)
            if char == 'R':
                r_ids.append(i)
        
        while 0 < len(l_ids) or 0 < len(r_ids):
            for li in l_ids:
                arr[li] -= 1
            for ri in r_ids:
                arr[ri] += 1
            new_l_ids, new_r_ids = [], []
            for li in l_ids:
                if 0 <= li-1 and arr[li-1] == 0:
                    new_l_ids.append(li-1)
            for ri in r_ids:
                if ri+1 < N and arr[ri+1] == 0:
                    new_r_ids.append(ri+1)
            l_ids, r_ids = new_l_ids, new_r_ids
        
        res = []
        for num in arr:
            if num == 1:
                res.append('R')
            elif num == -1:
                res.append('L')
            else:
                res.append('.')
        return ''.join(res)
        
