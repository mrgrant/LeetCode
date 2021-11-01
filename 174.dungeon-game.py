#
# @lc app=leetcode id=174 lang=python
#
# [174] Dungeon Game
#

# @lc code=start
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon)
        n = len(dungeon[0])
        dp1 = [[[0] for _ in range(n)] for _ in range(m)]
        dp2 = [[[0] for _ in range(n)] for _ in range(m)]
        dir = [[0, -1], [-1, 0]]
        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    dp1[0][0] = dungeon[0][0]
                    dp2[0][0] = dungeon[0][0]
                else:
                    cur_h = float("-inf")
                    min_h = float("-inf")
                    for dx, dy in dir:
                        mx = i + dx
                        my = j + dy
                        if mx >= 0 and my >= 0:
                            cur_h = max(cur_h, dp1[mx][my][0])
                            min_h = max(min_h, dp2[mx][my][1])
                    dp1[i][j] = cur_h + dungeon[i][j]
                    dp2[i][j] = min(min_h, dp2[i][j][0])
        return dp[-1][-1]

        
# @lc code=end

