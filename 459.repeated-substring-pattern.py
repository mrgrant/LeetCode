#
# @lc app=leetcode id=459 lang=python
#
# [459] Repeated Substring Pattern
#

# @lc code=start
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ss = s[1:] + s[:-1]
        return s in ss
        
# @lc code=end

