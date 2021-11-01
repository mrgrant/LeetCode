#
# @lc app=leetcode id=368 lang=python
#
# [368] Largest Divisible Subset
#

# @lc code=start
class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = sorted(nums)
        dp = [[i] for i in nums]
        for i in range(1, len(nums)):
            for j in range(i)[::-1]:
                if nums[i] % nums[j] == 0 and len(dp[i]) < len(dp[j]) + 1:
                    dp[i] = dp[j] + [nums[i]]
        return max(dp, key=len)
# @lc code=end

