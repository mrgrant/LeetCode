#
# @lc app=leetcode id=46 lang=python
#
# [46] Permutations
#

# @lc code=start
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        def dfs(arr, temp):
            if not arr:
                self.res.append(temp)
                return 
            for i in range(len(nums)):
                temp.append(nums[i])
                dfs(nums[:i]+nums[i+1:], temp)
                temp.pop()
            return
        dfs(nums, [])
        return self.res
if __name__ == "__main__":
    obj = Solution()
    a = obj.permute([1, 2, 3])
        
# @lc code=end

