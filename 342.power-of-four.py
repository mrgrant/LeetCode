#
# @lc app=leetcode id=342 lang=python
#
# [342] Power of Four
#

# @lc code=start
class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = set()
        c = 1
        while n >= c:
            if n == c:
                return True
            c *= 4
        return False
        
# @lc code=end

