#
# @lc app=leetcode id=1041 lang=python
#
# [1041] Robot Bounded In Circle
#

# @lc code=start
class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        l = {(0, 1): (-1, 0), (-1, 0): (0, -1), (0, -1): (1, 0), (1, 0): (0, 1)}
        r = {(0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0, 1)}
        visit = set()
        visit.add((0, 0))
        cur = [0, 0]
        dir = (0, 1)
        for i, c in enumerate(instructions * 4):
            if c == "G":
                cur[0] += dir[0]
                cur[1] += dir[1]
            elif c == "L":
                dir = l[dir]
            elif c == "R":
                dir = r[dir]
            
            if (i + 1) % len(instructions ) == 0:
                cur_tuple = (cur[0], cur[1])
                if cur_tuple in visit:
                    return True
                else:
                    visit.add(cur_tuple)
        return False
        
# @lc code=end

