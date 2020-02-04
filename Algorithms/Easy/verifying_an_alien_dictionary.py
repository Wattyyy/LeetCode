# https://leetcode.com/problems/verifying-an-alien-dictionary/

class Solution:    
    def isAlienSorted(self, words, order):
        order_dic = {}
        i = 1
        for char in order:
            order_dic[char] = str(i+10)
            i += 1
            
        def encode_word(word, max_len):
            res = list(word)
            for i in range(len(res)):
                res[i] = order_dic[res[i]]
            res = res + ["00"] * (max_len - len(res))
            return int("".join(res))
        
        max_len = max([len(word) for word in words])
        encoded_list = [encode_word(word, max_len) for word in words]
        for i in range(1, len(encoded_list)):
            if encoded_list[i-1] > encoded_list[i]:
                return False
        return True

