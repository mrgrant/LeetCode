#
# @lc app=leetcode id=999 lang=python
#
# [999] Available Captures for Rook
#

# @lc code=start
class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        m = len(board)
        n = len(board[0])
        rook = None
        for i in range(m):
            for j in range(n):
                if board[i][j] == "R":
                    rook = [i, j]
        def dfs(rook, dir, m, n):
            dx = rook[0] + dir[0]
            dy = rook[1] + dir[1]
            while 0 <= dx < m and 0 <= dy < n:
                if board[dx][dy] == "B":
                    return 0
                elif board[dx][dy] == "p":
                    return 1
                dx += dir[0]
                dy += dir[1]
            return 0
        res = dfs(rook, [0, 1], m, n) + dfs(rook, [0, -1], m, n) + dfs(rook, [1, 0], m, n) + dfs(rook, [-1, 0], m, n)
        return res

        
# @lc code=end
if __name__ == "__main__":
    obj = Solution()
    board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
    a = obj.numRookCaptures(board) 

