class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        ret = []
        nums = sorted(nums)
        # two pointer
        for i in range(len(nums) - 2):
            if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                lo = i + 1
                hi = len(nums) - 1
                target = -nums[i]
                while lo < hi:
                    if nums[lo] + nums[hi] == target:
                        ret.append([nums[i], nums[lo], nums[hi]])
                        while lo < hi and nums[lo] == nums[lo + 1]:
                            lo += 1
                        while lo < hi and nums[hi] == nums[hi - 1]:
                            hi -= 1
                        lo += 1
                        hi -= 1
                    elif nums[lo] + nums[hi] < target:
                        while lo < hi and nums[lo] == nums[lo + 1]:
                            lo += 1
                        lo += 1
                    else:
                        while lo < hi and nums[hi] == nums[hi - 1]:
                            hi -= 1
                        hi -= 1
        return ret

if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    obj = Solution()
    a = obj.threeSum(nums)