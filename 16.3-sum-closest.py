#
# @lc app=leetcode id=16 lang=python
#
# [16] 3Sum Closest
#

# @lc code=start


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        ret = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == target:
                    return target
                elif sum > target:
                    k -= 1
                else:
                    j += 1
                if abs(sum - target) < abs(ret - target):
                    ret = sum
        return ret

        



# @lc code=end

