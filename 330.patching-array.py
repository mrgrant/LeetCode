#
# @lc app=leetcode id=330 lang=python
#
# [330] Patching Array
#

# @lc code=start
class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        cnt = 0
        maxReach = 0
        for i in range(len(nums)):
            
            while maxReach + 1 < nums[i]:
                maxReach = maxReach + (maxReach + 1)
                cnt += 1
                if maxReach >= n:
                    break
            maxReach += nums[i]          
            if maxReach >= n:
                break
        while maxReach < n:
            maxReach = maxReach + (maxReach + 1)
            cnt += 1
        return cnt

# @lc code=end

if __name__ ==  "__main__":
    obj = Solution()
    nums = [1,2,2,6,34,38,41,44,47,47,56,59,62,73,77,83,87,89,94]
    n = 20
    a = obj.minPatches(nums, n)