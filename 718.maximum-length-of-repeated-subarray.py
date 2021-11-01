#
# @lc app=leetcode id=718 lang=python
#
# [718] Maximum Length of Repeated Subarray
#

# @lc code=start
class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        dp = [[0 for _ in range(len(nums2)+1)] for _ in range(len(nums1)+1)]
        for i in range(1, len(nums1)+1):
            for j in range(1, len(nums2)+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
        return max(max(row) for row in dp)
        
# @lc code=end
if __name__ == "__main__":
    obj = Solution()
    a = obj.findLength([1,2,3,2,1], [3,2,1,4,7])

