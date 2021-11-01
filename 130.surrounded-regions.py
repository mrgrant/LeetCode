#
# @lc app=leetcode id=130 lang=python
#
# [130] Surrounded Regions
#

# @lc code=start
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        visit = set()
        for i in range(m):
            for j in range(n):
                if board[i][j] == "X":
                    continue
                elif (i, j) not in visit:
                    visit.add((i, j))
                    flip = True
                    olist = [[i, j]]
                    stack = [[i, j]]
                    if i == 0 or i == m-1 or j == 0 or j == n-1:
                        flip = False
                    while stack:
                        temp = []
                        for x, y in stack:
                            for dx, dy in dir:
                                mx = x + dx
                                my = y + dy
                                if  0 <= mx < m and 0 <= my < n and board[mx][my] == "O" and (mx, my) not in visit:
                                    visit.add((mx, my))
                                    temp.append([mx, my])
                                    olist.append([mx, my])
                                    if mx == 0 or mx == m-1 or my == 0 or my == n-1:
                                        flip = False
                        stack = temp
                    if flip:
                        for x, y in olist:
                            board[x][y] = "X"
        return board




        
# @lc code=end

