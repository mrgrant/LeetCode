#
# @lc app=leetcode id=396 lang=python
#
# [396] Rotate Function
#

# @lc code=start
class Solution(object):
    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = sum(nums)
        f0 = [i * n for i, n in enumerate(nums)]
        f0 = sum(f0)
        _max = f0
        for i in range(len(nums))[::-1]:
            f = f0 + s - len(nums) * nums[i]
            _max = max(_max, f)
            f0 = f
        return _max

        
# @lc code=end

