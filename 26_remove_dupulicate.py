class Solution:
    def removeDuplicates(self, nums):
        l = len(nums)
        if l <= 1:
            return l
        else:
            s = 0
            for i in range(1,l):
                if nums[s] != nums[i]:
                    s += 1
                    nums[s] = nums[i]
        return s + 1    
