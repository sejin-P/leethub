class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = []
        max_h = -1
        
        for i in range(n):
            idx = n-i-1
            if max_h < heights[idx]:
                max_h = heights[idx]
                res.append(idx)
        
        return reversed(res)  
        
        