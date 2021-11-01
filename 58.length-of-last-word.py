#
# @lc app=leetcode id=58 lang=python
#
# [58] Length of Last Word
#

# @lc code=start
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        slist = s.split()
        if not slist:
            return 0
        return len(slist[-1])
        
# @lc code=end

