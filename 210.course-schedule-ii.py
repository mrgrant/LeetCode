#
# @lc app=leetcode id=210 lang=python
#
# [210] Course Schedule II
#

# @lc code=start
import collections
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        self.graph = collections.defaultdict(list)
        for x, y in prerequisites:
            # dfs的尽头是第一门课
            self.graph[x].append(y)
        # 0 代表未经过，1代表已经结束，-1代表dfs时经过，用于排除环
        self.visited = [0 for _ in range(numCourses)]
        self.res = []

        for i in range(numCourses):
            if not self.dfs(i):
                return []
            # 鸡血遍历剩下的节点
        return self.res

    def dfs(self, node):
        if self.visited[node] == -1:
            return False # 有环
        if self.visited[node] == 1:
            return True # 已经遍历过该节点
        self.visited[node] = -1
        for n in self.graph[node]:
            if not self.dfs(n):
                return False 
        self.visited[node] = 1
        self.res.append(node)
        return True    

        

# @lc code=end

