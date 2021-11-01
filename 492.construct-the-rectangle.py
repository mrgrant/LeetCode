#
# @lc app=leetcode id=492 lang=python
#
# [492] Construct the Rectangle
#

# @lc code=start
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        ret = [area, 1]
        i = 1
        while i * i <= area:
            if area % i == 0:
                ret = [area//i, i]
            i += 1
        return ret
        
# @lc code=end

