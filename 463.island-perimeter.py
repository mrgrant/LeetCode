#
# @lc app=leetcode id=463 lang=python
#
# [463] Island Perimeter
#

# @lc code=start
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        m = len(grid)
        n = len(grid[0])
        ret = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cnt = 0
                    for dx, dy in dir:
                        mx = dx + i
                        my = dy + j
                        if 0 <= mx < m and 0 <= my < n:
                            if grid[mx][my] == 1:
                                cnt += 1
                    ret += (4 - cnt) 
        return ret
            
# @lc code=end

