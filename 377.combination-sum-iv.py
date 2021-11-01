#
# @lc app=leetcode id=377 lang=python
#
# [377] Combination Sum IV
#

# @lc code=start
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0 for _ in range(target+1)]
        dp[0] = 1
        for i in range(1, len(dp)):
            for n in nums:
                if i - n < 0:
                    continue
                else:
                    dp[i] += dp[i-n]
        return dp[target]

# @lc code=end

