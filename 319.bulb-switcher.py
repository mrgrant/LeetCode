#
# @lc app=leetcode id=319 lang=python
#
# [319] Bulb Switcher
#

# @lc code=start
import math
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(math.sqrt(n))
# @lc code=end

