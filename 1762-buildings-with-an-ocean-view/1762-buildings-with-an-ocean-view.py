class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = []
        max_h = -1
        
        for i in range(n):
            if max_h < heights[n-i-1]:
                max_h = heights[n-i-1]
                res.append(n-i-1)
        
        return reversed(res)  
        
        