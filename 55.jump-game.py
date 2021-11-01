#
# @lc app=leetcode id=55 lang=python
#
# [55] Jump Game
#

# @lc code=start
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        farest = 0
        for i in range(len(nums)-1):
            farest = max(farest, i + nums[i])
            if farest <= i:
                return False
        return farest >= len(nums) - 1
        

# @lc code=end

