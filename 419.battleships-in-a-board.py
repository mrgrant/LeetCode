#
# @lc app=leetcode id=419 lang=python
#
# [419] Battleships in a Board
#

# @lc code=start
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        m = len(board)
        n = len(board[0])
        move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        cnt = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == "X":
                    cnt += 1
                    dx = dy = 0
                    for d in move:
                        mx = i + d[0]
                        my = j + d[1]
                        if 0 <= mx < m and 0 <= my < n and board[mx][my] == "X":
                            dx = d[0]
                            dy = d[1]
                    curi= i
                    curj = j
                    while 0 <= curi < m and 0 <= curj < n and board[curi][curj] == "X":
                        board[curi][curj] = "."
                        curi += dx
                        curj += dy
        return cnt

        
# @lc code=end

