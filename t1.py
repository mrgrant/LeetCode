class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        p = {}
        for i in range(n):
            if nums[i] in p:
                return p[nums[i]],i
            else:
                p[target - nums[i]] = i

