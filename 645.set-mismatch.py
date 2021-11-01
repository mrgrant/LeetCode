#
# @lc app=leetcode id=645 lang=python
#
# [645] Set Mismatch
#

# @lc code=start
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        li = [0 for _ in range(len(nums))]
        for n in nums:
            li[n-1] += 1
        ret = [0, 0]
        for i in range(len(nums)):
            if li[i] == 0:
                ret[1] = i+1
            if li[i] == 2:
                ret[0] = i + 1
        return ret 
# @lc code=end

