#
# @lc app=leetcode id=969 lang=python
#
# [969] Pancake Sorting
#

# @lc code=start
class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        self.res = []
        self.sort(arr, len(arr))
        return self.res
    
    def sort(self, arr, n):
        if n == 1:
            return
        max_idx = 0
        amax = 0
        for i in range(len(arr)):
            if arr[i] > amax:
                max_idx = i
                amax = arr[i]
        arr = self.reverse(arr, 0, max_idx)
        arr = self.reverse(arr, 0, len(arr)-1)
        self.res.append(max_idx+1)
        self.res.append(len(arr))
        self.sort(arr[:n-1], n-1)


    def reverse(self, arr, i, j):
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        return arr

        
# @lc code=end
if __name__ == "__main__":
    obj = Solution()
    a = obj.pancakeSort([3, 2, 4, 1])
