#
# @lc app=leetcode id=18 lang=python
#
# [18] 4Sum
#

# @lc code=start



class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        retList = []
        last = None
        for i in range(len(nums)):
            if last == nums[i]:
                continue
            last = nums[i]
            self.threeSum(nums, target-nums[i], i, retList)
        return retList

    def threeSum(self, nums, target, start, retList):
        lastI = None
        for i in range(start+1, len(nums)):
            if lastI == nums[i]:
                continue
            lastI = nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                left = nums[j]
                right = nums[k]
                if sum < target:
                    while j < k and left == nums[j]:
                        j += 1
                elif sum > target:
                    while j < k and right == nums[k]:
                        k -= 1
                else:
                    retList.append([nums[start], nums[i], nums[j], nums[k]])
                    while j < k and left == nums[j]:
                        j += 1
                    while j < k and right == nums[k]:
                        k -= 1

# @lc code=end

if __name__ == "__main__":
    obj = Solution()
    a = obj.fourSum([1,0,-1,0,-2,2], 0)

