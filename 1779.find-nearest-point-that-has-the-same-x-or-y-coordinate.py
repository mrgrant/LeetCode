#
# @lc app=leetcode id=1779 lang=python
#
# [1779] Find Nearest Point That Has the Same X or Y Coordinate
#

# @lc code=start
class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        res = float("inf")
        idx = -1
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                dis = abs(points[i][0] - x) + abs(points[i][1] - y)
                if dis < res:
                    idx = i
                    res = dis
        return idx

# @lc code=end

