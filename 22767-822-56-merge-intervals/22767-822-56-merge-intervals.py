class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        
        intervals.sort(key=lambda x: x[0])

        prev = intervals[0]
        res = []

        for interval in intervals[1:]:
            if interval[0] > prev[1]:
                res.append(prev)
                prev= interval
                continue
            
            prev[1] = max(interval[1], prev[1])
            
        if prev:
            res.append(prev)

        return res
        