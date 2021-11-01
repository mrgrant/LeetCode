#
# @lc app=leetcode id=780 lang=python
#
# [780] Reaching Points
#

# @lc code=start
class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        while sx < tx and sy < ty:
            if tx < ty:
                ty = ty % tx
            else:
                tx = tx % ty
        return (sy == ty and tx >= sx and (tx - sx) % sy == 0) or (sx == tx and ty >= sy and (ty - sy) % sx == 0)

# @lc code=end

