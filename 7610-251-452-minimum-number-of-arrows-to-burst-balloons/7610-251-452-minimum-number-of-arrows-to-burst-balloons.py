class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1

        points.sort(key=lambda x: x[0])

        prev = points[0]
        res = 0

        for point in points:
            if point[0] > prev[1]:
                res += 1
                prev = point
                continue
            
            if prev[1] > point[1]:
                prev[1] = point[1]
            if prev[0] < point[0]:
                prev[0] = point[0]

        if prev:
            res += 1
        
        return res
        
        