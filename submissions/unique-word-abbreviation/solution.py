# https://leetcode.com/problems/unique-word-abbreviation

from collections import defaultdict
class ValidWordAbbr:
    def __init__(self, dictionary):
        self.dic = defaultdict(set)
        for word in dictionary:
            N = len(word)
            if N <= 2:
                self.dic[word].add(word)
            else:
                val = word[0] + str(N-2) + word[-1]
                self.dic[val].add(word)

    def isUnique(self, word):
        N = len(word)
        if N <= 2:
            val = word
        else:
            val = word[0] + str(N-2) + word[-1]
        return ( (not self.dic[val]) or (word in self.dic[val] and len(self.dic[val]) == 1) )
    


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)