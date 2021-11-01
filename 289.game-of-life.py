#
# @lc app=leetcode id=289 lang=python
#
# [289] Game of Life
#

# @lc code=start
from typing import Mapping


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        move = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                live = 0
                for dx, dy in move:
                    mx = i + dx
                    my = j + dy
                    if 0 <= mx < m and 0 <= my < n:
                        if board[i][j] == 1 or board[i][j] == 3:
                            live += 1
                if board[i][j] == 1:
                    if live < 2 or live > 3:
                        board[i][j] = 3
                else:
                    if live == 3:
                        board[i][j] = 4
        for i in range(m):
            for j in range(n):
                if board[i][j] == 3:
                    board[i][j] = 0
                elif board[i][j] == 4:
                    board[i][j] = 1
    
# @lc code=end
if __name__ == "__main__":
    obj = Solution()
    obj.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])
