#
# @lc app=leetcode id=673 lang=python
#
# [673] Number of Longest Increasing Subsequence
#

# @lc code=start
class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1 for _ in range(len(nums))]
        path = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            smax = 1
            cnt = 0
            for j in range(i)[::-1]:
                if nums[i] > nums[j]:
                    smax = max(smax, dp[j]+1)
            for j in range(i)[::-1]:
                if nums[i] > nums[j] and dp[j] == smax - 1:
                    cnt += path[j]
            dp[i] = smax
            path[i] = cnt if cnt else 1
        smax = max(dp)
        res = 0
        for i in range(len(dp)):
            if dp[i] == smax:
                res += path[i]
        return res 
        
# @lc code=end

