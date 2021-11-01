#
# @lc app=leetcode id=621 lang=python
#
# [621] Task Scheduler
#

# @lc code=start
import heapq
import collections
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if n == 0:
            return len(tasks)
        d = collections.defaultdict(int)
        for c in tasks:
            d[c] += 1
        heap = []
        for key in d:
            heap.append([-d[key], 0])
        heapq.heapify(heap)
        cooldown = []
        cnt = 0
        while cooldown or heap:
            temp = []
            if heap:
                task = heapq.heappop(heap)
                task[0] += 1
                task[1] = n
                if task[0] < 0:
                    temp.append(task)
            for task in cooldown:
                task[1] -= 1
                if task[1] == 0:
                    heapq.heappush(heap, task)
                else:
                    temp.append(task)
            cooldown = temp
            cnt += 1
        return cnt
        
# @lc code=end

if __name__ == "__main__":
    obj = Solution()
    a = obj.leastInterval(["A","A","A","B","B","B"], 2)