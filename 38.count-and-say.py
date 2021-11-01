#
# @lc app=leetcode id=38 lang=python
#
# [38] Count and Say
#

# @lc code=start
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        res = "1"
        for _ in range(n-1):
            temp = ""
            pre = res[0]
            cnt = 1
            for i, c in enumerate(res):
                if i == 0:
                    continue
                if c == pre:
                    cnt += 1
                else:
                    temp += str(cnt) + pre
                    pre = c
                    cnt = 1
            temp += str(cnt) + pre
            res = temp
        return res

if __name__ == "__main__":
    obj = Solution()
    a = obj.countAndSay(4)

# @lc code=end

