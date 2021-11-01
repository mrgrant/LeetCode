#
# @lc app=leetcode id=452 lang=python
#
# [452] Minimum Number of Arrows to Burst Balloons
#

# @lc code=start
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points = sorted(points, key=(lambda x:x[1]))
        count = 1
        end = points[0][1]
        for x in points:
            if x[0] <= end:
                continue
            else:
                end = x[1]
                count += 1
        return count

        
# @lc code=end

