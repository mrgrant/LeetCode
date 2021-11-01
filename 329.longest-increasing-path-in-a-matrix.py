#
# @lc app=leetcode id=329 lang=python
#
# [329] Longest Increasing Path in a Matrix
#

# @lc code=start
import collections
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        # dfs solution
        # m = len(matrix)
        # n = len(matrix[0])
        # dp = [[0 for _ in range(n)] for _ in range(m)]
        # def dfs(i, j):
        #     if not dp[i][j]:
        #         val = matrix[i][j]
        #         dp[i][j] = 1 + max(
        #             dfs(i-1,j) if i > 0 and matrix[i-1][j] < val else 0,
        #             dfs(i+1,j) if i < m - 1 and matrix[i+1][j] < val else 0,
        #             dfs(i,j-1) if j > 0 and matrix[i][j-1] < val else 0,
        #             dfs(i,j+1) if j < n - 1 and matrix[i][j+1] < val else 0,
        #         )
        #     return dp[i][j]
        # for i in range(m):
        #     for j in range(n):
        #         dfs(i, j)
        # return max(dp[i][j] for i in range(m) for j in range(n))
        
        # bfs with topological sort solution    
           
        m = len(matrix)
        n = len(matrix[0])
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        indeg = {}
        q = collections.deque()
        for i in range(m):
            for j in range(n):
                cnt = 0
                for dx, dy in dir:
                    mx = i + dx
                    my = j + dy
                    if 0 <= mx < m and 0 <= my < n and matrix[mx][my] < matrix[i][j]:
                        cnt += 1
                indeg[(i, j)] = cnt
                if cnt == 0:
                    q.append((i, j))
        step = 0
        while q:
            size = len(q)
            for _ in range(size):
                x, y = q.popleft()
                for dx, dy in dir:
                    mx = x + dx
                    my = y + dy
                    if 0 <= mx < m and 0 <= my < n and matrix[mx][my] > matrix[x][y] and (mx, my) in indeg:
                        indeg[(mx, my)] -= 1
                        if indeg[(mx, my)] == 0:
                            q.append((mx, my))     
            step += 1
        return step                   

# @lc code=end

