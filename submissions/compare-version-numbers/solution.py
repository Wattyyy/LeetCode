# https://leetcode.com/problems/compare-version-numbers

class Solution:
    def compareVersion(self, version1, version2):
        v1_list = version1.split('.')
        v2_list = version2.split('.')
        if len(v1_list) <= len(v2_list):
            for _ in range(len(v2_list) - len(v1_list)):
                v1_list.append('0')
        else:
            for _ in range(len(v1_list) - len(v2_list)):
                v2_list.append('0')
        
        v1_list = list(map(int, v1_list))
        v2_list = list(map(int, v2_list))
        v1_int = int( ''.join( list(map(str, v1_list)) ) )
        v2_int = int( ''.join( list(map(str, v2_list)) ) )
        
        if v1_int > v2_int:
            return 1
        elif v1_int == v2_int:
            return 0
        else:
            return -1