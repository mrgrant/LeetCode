#
# @lc app=leetcode id=1465 lang=python
#
# [1465] Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
#

# @lc code=start
class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        horizontalCuts = sorted(horizontalCuts + [0, h])
        verticalCuts = sorted(verticalCuts + [0, w])
        maxh = 0 
        maxw = 0
        for i in range(1, len(horizontalCuts)):
            if horizontalCuts[i] - horizontalCuts[i-1] > maxh:
                maxh = horizontalCuts[i] - horizontalCuts[i-1]
        for i in range(1, len(verticalCuts)):
            if verticalCuts[i] - verticalCuts[i-1] > maxw:
                maxw = verticalCuts[i] - verticalCuts[i-1]
        return (maxh * maxw) % (10**9 + 7)
        

# @lc code=end

