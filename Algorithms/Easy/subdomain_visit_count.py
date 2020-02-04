# https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains):
        dic = {}
        for cp in cpdomains:
            num, domain = cp.split(" ")
            domain_list = domain.split(".")
            N = len(domain_list)
            for i in range(N):
                key = ".".join(domain_list[i:N])
                if key not in dic.keys():
                    dic[key] = 0    
                dic[key] += int(num)
        
        ans = []
        for k, v in dic.items():
            string = str(v) + " " + k
            ans.append(string)
        return ans
                
                
