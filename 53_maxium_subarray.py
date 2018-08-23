class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        for i in range(1,length):
            maxsub = max(nums[i]+nums[i-1], nums[i])
            nums[i] = maxsub
        return max(nums)
# using O(n) times


if __name__ == '__main__':
    a = [-2,1,-3,4,-1,2,1,-5,4]
    print(Solution().maxSubArray(a))