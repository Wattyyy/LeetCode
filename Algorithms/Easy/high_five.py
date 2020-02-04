# https://leetcode.com/problems/high-five/

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        dic = {}
        for item in items:
            s_id = item[0]
            score = item[1]
            if s_id not in dic.keys(): dic[s_id] = []
            dic[s_id].append(score)
        
        ans_dic = {}
        for key in dic.keys():
            sorted_list = sorted(dic[key], reverse=True)
            mean_score = sum(sorted_list[:5])//5
            ans_dic[key] = mean_score
        
        output = []
        keys = sorted(ans_dic.keys())
        for key in keys:
            output.append([key, ans_dic[key]])
        return output
