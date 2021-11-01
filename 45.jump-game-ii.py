#
# @lc app=leetcode id=45 lang=python
#
# [45] Jump Game II
#

# @lc code=start
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 这一次跳的最远距离
        end = 0
        farest = 0
        count = 0
        for i in range(len(nums)-1):
            farest = max(farest, i + nums[i])
            # 代表第n次跳跃结束
            if i == end:
                count += 1
                end = farest
        return count

        
# @lc code=end
if __name__ == "__main__":
    obj = Solution()
    a = obj.jump([2,3,1,1,4])

