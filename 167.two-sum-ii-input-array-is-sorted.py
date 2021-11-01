#
# @lc app=leetcode id=167 lang=python
#
# [167] Two Sum II - Input array is sorted
#

# @lc code=start
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        def bin_search(numbers, start, end, target):
            l = start
            r = end 
            while l < r:
                print(l)
                mid = (l + r) // 2
                if numbers[mid] < target:
                    l = mid + 1
                else:
                    r = mid 
            return l
        for i in range(len(numbers)):
            n = bin_search(numbers, i+1, len(numbers), target-numbers[i])
            if n < len(numbers) and numbers[i] + numbers[n] == target:
                return [i+1, n+1]
        return [0, 0]
        
# @lc code=end

if __name__ == "__main__":
    obj = Solution()
    obj.twoSum([5, 25, 75], 100)