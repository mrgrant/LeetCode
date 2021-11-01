#
# @lc app=leetcode id=80 lang=python
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre = nums[0]
        cnt = 0
        for i, n in enumerate(nums):
            if pre != n:
                pre = n
                cnt = 0
            elif pre == n:
                cnt += 1
            if cnt > 2:
                nums[i] = "_"       
        nums.remove("_")
        return nums     

            
# @lc code=end

