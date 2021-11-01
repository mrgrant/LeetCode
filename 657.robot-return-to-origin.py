#
# @lc app=leetcode id=657 lang=python
#
# [657] Robot Return to Origin
#

# @lc code=start
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x = 0
        y = 0
        d = {"U": 1, "D": -1, "R": 1, "L": -1}
        for c in moves:
            if c == "U" or c == "D":
                y += d[c]
            else:
                x += d[c]
        return x == 0 and y == 0
        
# @lc code=end

