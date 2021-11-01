#
# @lc app=leetcode id=670 lang=python
#
# [670] Maximum Swap
#

# @lc code=start
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        nlist = list(str(num))
        bucket = [0 for _ in range(10)]
        for i in range(len(nlist)):
            bucket[int(nlist[i])] = i
        for i in range(len(nlist)):
            for j in range(int(nlist[i])+1, 10)[::-1]:
                if bucket[j] > i:
                    nlist[i], nlist[bucket[j]] = nlist[bucket[j]], nlist[i]
                    return int(''.join(nlist))
        return num


# @lc code=end
if __name__ == "__main__":
    obj = Solution()
    obj.maximumSwap(98368)
