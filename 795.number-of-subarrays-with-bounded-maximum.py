#
# @lc app=leetcode id=795 lang=python
#
# [795] Number of Subarrays with Bounded Maximum
#

# @lc code=start
class Solution(object):
    def numSubarrayBoundedMax(self, nums, left, right):
        """
        :type nums: List[int]
        :type left: int
        :type right: int
        :rtype: int
        """
        def rightBound(nums, right):
            res = 0
            cnt = 0
            for i in range(len(nums)):
                if nums[i] <= right:
                    cnt += 1
                else:
                    cnt = 0
                res += cnt
            return res
        return rightBound(nums, right) - rightBound(nums, left - 1)
                    
# @lc code=end

