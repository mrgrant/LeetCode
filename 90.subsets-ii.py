#
# @lc app=leetcode id=90 lang=python
#
# [90] Subsets II
#

# @lc code=start
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        nums = sorted(nums)
        def dfs(nums, rList):
            if not nums:
                return 
            pre = None
            for i in range(len(nums)):
                if pre == nums[i]:
                    continue
                rList.append(nums[i])
                res.append(rList[:])
                pre = nums[i]
                dfs(nums[i+1:], rList)
                rList.pop()
            return 
        dfs(nums, [])
        return res
# @lc code=end

if __name__ == "__main__":
    obj = Solution()
    res = obj.subsetsWithDup([1, 2, 2])

