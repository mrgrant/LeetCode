#
# @lc app=leetcode id=1359 lang=python
#
# [1359] Count All Valid Pickup and Delivery Options
#

# @lc code=start
class Solution(object):
    def countOrders(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for _ in range(n+1)]
        dp[1]= 1
        for i in range(2, n+1):
            k = (i - 1) * 2 + 1
            dp[i] = ((k+1) * k // 2 * dp[i-1]) % (10**9 + 7)
        return dp[-1]


        
# @lc code=end

