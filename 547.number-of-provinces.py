#
# @lc app=leetcode id=547 lang=python
#
# [547] Number of Provinces
#

# @lc code=start
class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        m = len(isConnected)
        visit = set()
        def dfs(n):
            for i, val in enumerate(isConnected[n]):
                if val and i not in visit:
                    visit.add(i)
                    dfs(i)
                    

        res = 0
        for i in range(m):
            if i not in visit:
                dfs(i)
                res += 1
        return res

# @lc code=end

