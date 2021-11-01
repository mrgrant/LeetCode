import heapq
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        points = [(l, -h, r) for l, r, h in buildings] + [(r, 0, 0) for r in set(r for _, r, _ in buildings)]
        points = sorted(points)
        heap = [[0, float('inf')]]
        res = [[0, 0]]
        for l, h, r in points:
            while heap[0][1] <= l:
                heapq.heappop(heap)
            if h:
                heapq.heappush(heap, [h, r])
            if -heap[0][0] != res[-1][1]:
                res.append([l, -heap[0][0]])
        return res[1:]

if __name__ == "__main__":
    obj = Solution()
    buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    a = obj.getSkyline(buildings)