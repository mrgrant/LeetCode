#
# @lc app=leetcode id=443 lang=python
#
# [443] String Compression
#

# @lc code=start
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if not chars:
            return 0
        ret = ""
        pre = chars[0]
        cnt = 1
        for i in range(1, len(chars)):
            if chars[i] == pre:
                cnt += 1
            else:
                ret += pre
                if cnt != 1:
                    ret += str(cnt)
                cnt = 1
                pre = chars[i]
            if i == len(chars) - 1:
                ret += pre
                if cnt != 1:
                    ret += str(cnt)
        return len(ret)
if __name__ == "__main__":
    obj = Solution()
    a = obj.compress(["a","a","b","b","c","c","c"])
# @lc code=end

