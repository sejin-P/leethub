class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals
        if newInterval[0] > intervals[-1][1]:
            return intervals + [newInterval]
        
        left, right = [], []
        mergeMin, mergeMax = newInterval[0], newInterval[1]
        
        for interval in intervals:
            if interval[1] < newInterval[0]:
                left.append(interval)
            elif interval[0] > newInterval[1]:
                right.append(interval)
            
            else:
                mergeMin = min(mergeMin, interval[0])
                mergeMax = max(mergeMax, interval[1])
            
            
        return left + [[mergeMin, mergeMax]] + right
            
                
        