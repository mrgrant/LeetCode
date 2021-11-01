#
# @lc app=leetcode id=695 lang=python
#
# [695] Max Area of Island
#

# @lc code=start
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and  grid[i][j] == 1:
                grid[i][j] = 2
                return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)
            else:
                return 0
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cnt = dfs(i, j)
                    res = max(cnt, res)
        return res
# @lc code=end

