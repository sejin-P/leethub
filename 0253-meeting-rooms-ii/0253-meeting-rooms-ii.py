import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 1
        intervals.sort(key=lambda x: x[0])
        
        h = [intervals[0][1]]
        heapq.heapify(h)
        res = 1
        
        for interval in intervals[1:]:
            if h[0] > interval[0]:
                heapq.heappush(h, interval[1])
                res = max(res, len(h))
                continue
            
            while h and h[0] <= interval[0]:
                heapq.heappop(h)
            
            heapq.heappush(h, interval[1])
                
        return res
            
            