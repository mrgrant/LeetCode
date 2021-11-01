#
# @lc app=leetcode id=554 lang=python
#
# [554] Brick Wall
#

# @lc code=start
class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        m = len(wall)
        wall_len = sum(wall[0])
        presum = [[] for _ in range(m)]
        for i in range(m):
            for j, n in enumerate(wall[i]):
                if j == 0:
                    presum[i].append(n)
                else:
                    presum[i].append(presum[i][-1] + n)
        d = {}
        for i in range(m):
            for n in presum[i]:
                if n != wall_len and n not in d:
                    d[n] = 1
                elif n in d:
                    d[n] += 1
        smax = 0
        for key in d:
            smax = max(smax, d[key])
        return m - smax

# @lc code=end