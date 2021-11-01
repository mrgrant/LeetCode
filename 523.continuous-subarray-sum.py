#
# @lc app=leetcode id=523 lang=python
#
# [523] Continuous Subarray Sum
#

# @lc code=start
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        presum = [0 for _ in range(len(nums) + 1)]
        for i in range(len(nums)):
            presum[i+1] = presum[i] + nums[i]
        d = {0: 0}
        for i, n in enumerate(presum):
            mod = n % k
            if mod in d:
                if i - d[mod] > 1:
                    return True
            else:
                d[mod] = i
        return False

# @lc code=end

