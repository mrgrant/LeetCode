import heapq
class Solution:
    def meetingRoom(self, intervals):
        intervals = sorted(intervals, key = lambda x:x[0])
        end = []
        heapq.heapify(end)
        for s, e in intervals:
            if len(end) == 0:
                heapq.heappush(end, e)
            else:
                if s >= end[0]:
                    heapq.heappop(end)
                    heapq.heappush(end, e)
                else:
                    heapq.heappush(end, e)
        return len(end)

if __name__ == "__main__":
    obj = Solution()
    a = obj.meetingRoom([[0, 30],[5, 10],[15, 20]])
    print(a)
    
