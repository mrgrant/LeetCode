#
# @lc app=leetcode id=977 lang=python
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        min_idx = 0
        nmin = float("inf")
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = -nums[i]
            if nums[i] < nmin:
                nmin = nums[i]
                min_idx = i
        j = min_idx
        i = j - 1

        while i >= 0 or j < len(nums):
            if i < 0 and j < len(nums):
                res.append(nums[j] ** 2)
                j += 1
            if j >= len(nums) and i >= 0:
                res.append(nums[i] ** 2)
                i -= 1
            if i >= 0 and j < len(nums) and nums[i] < nums[j]:
                res.append(nums[i] ** 2)
                i -= 1
            elif i >= 0 and j < len(nums) and nums[i] >= nums[j]:
                res.append(nums[j] ** 2)
                j += 1
        return res

# @lc code=end

