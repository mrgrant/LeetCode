#
# @lc app=leetcode id=391 lang=python
#
# [391] Perfect Rectangle
#

# @lc code=start
class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        x1, y1 = float('inf'), float('inf')
        x2, y2 = float('-inf'), float('-inf')
        s = set()
        sp = 0
        for x, y, a, b in rectangles:
            x1, y1 = min(x1, x), min(y1, y)
            x2, y2 = max(x2, a), max(y2, b)
            p1 = (x, y)
            p2 = (x, b)
            p3 = (a, y)
            p4 = (a, b)
            for p in [p1, p2, p3, p4]:
                if p not in s:
                    s.add(p)
                else:
                    s.remove(p)
            sp += (a-x) * (b-y)
        if len(s) != 4:
            return False
        if (x2 - x1) * (y2 - y1) != sp:
            return False
        if (x1, y1) not in s:
            return False
        if (x1, y2) not in s:
            return False
        if (x2, y1) not in s:
            return False
        if (x2, y2) not in s:
            return False
        return True
                

# @lc code=end

