def peaksToIntervals(peaks):
    res = []
    for peak in peaks:
        res.append([peak[0]-peak[1], peak[0]+peak[1]])
    return res

class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        intervals = []
        for x, y in peaks:
            intervals.append((x - y, x + y))
        intervals.sort(key=lambda i: (i[0], -i[1]))

        ans = 0
        max_end = -inf
        for i in range(len(intervals)):
            start, end = intervals[i]
            next_is_same = (i < len(intervals) - 1 and intervals[i+1] == intervals[i])
            ans += (end > max_end and not next_is_same)
            max_end = max(end, max_end)
        return ans