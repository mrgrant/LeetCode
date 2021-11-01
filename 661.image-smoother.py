#
# @lc app=leetcode id=661 lang=python
#
# [661] Image Smoother
#

# @lc code=start
class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(img)
        n = len(img[0])
        dx_list = [-1, 0, 1]
        dy_list = [-1, 0, 1]
        smooth = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                s = 0
                cnt = 0
                for dx in dx_list:
                    for dy in dy_list:
                        if 0 <= dx + i < m and 0 <= dy + j < n:
                            s += img[dx+i][dy+j]
                            cnt += 1
                smooth[i][j] = s // cnt
        return smooth


# @lc code=end

