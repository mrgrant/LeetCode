#
# @lc app=leetcode id=402 lang=python
#
# [402] Remove K Digits
#

# @lc code=start
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if len(num) == k:
            return "0"
        
# @lc code=end

