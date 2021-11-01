#
# @lc app=leetcode id=676 lang=python
#
# [676] Implement Magic Dictionary
#

# @lc code=start
import collections
class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        

    def buildDict(self, dictionary):
        """
        :type dictionary: List[str]
        :rtype: None
        """
        for word in dictionary:
            if len(word) not in self.d:
                self.d[len(word)] = collections.defaultdict(list)
            for i in range(len(word)):
                self.d[len(word)][word[:i] + "*" + word[i+1:]].append(word)
        

    def search(self, searchWord):
        """
        :type searchWord: str
        :rtype: bool
        """
        if len(searchWord) not in self.d:
            return False
        for i in range(len(searchWord)):
            word = searchWord[:i] + "*" + searchWord[i+1:]
            if word in self.d[len(searchWord)] and searchWord not in self.d[len(searchWord)][word]:
                return True
            elif word in self.d[len(searchWord)] and searchWord in self.d[len(searchWord)][word] and len(self.d[len(searchWord)][word]) > 1:
                return True
        return False 
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
# @lc code=end

