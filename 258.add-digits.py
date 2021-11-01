#
# @lc app=leetcode id=258 lang=python
#
# [258] Add Digits
#

# @lc code=start
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num // 10 != 0:
            d = num
            s = 0
            while d > 0:
                s += d % 10
                d /= 10
            num = s
        return num
        
# @lc code=end

