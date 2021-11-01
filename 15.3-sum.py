#
# @lc app=leetcode id=15 lang=python
#
# [15] 3Sum
#

# @lc code=start
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        ret = []
        old = None
        for i in range(len(nums)):
            if old == nums[i]:
                continue
            twoSumResult = self.twoSum(nums, -nums[i], i+1)
            ret.extend(twoSumResult)
            old = nums[i]
        return ret


    def twoSum(self, nums, target, start):
        lo = start
        hi = len(nums) - 1
        ret = []
        while lo < hi:
            sum = nums[lo] + nums[hi]
            left = nums[lo]
            right = nums[hi]
            if sum < target:
                while lo < hi and left == nums[lo]:
                    lo += 1
            elif sum > target:
                while lo < hi and right == nums[hi]:
                    hi -= 1
            else:
                ret.append([-target, nums[lo], nums[hi]])
                while lo < hi and left == nums[lo]:
                    lo += 1
                while lo < hi and right == nums[hi]:
                    hi -= 1
        return ret
        
# @lc code=end

