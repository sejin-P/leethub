class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        
        s = 0
        while l < r-1:
            mid = (l+r) // 2
        
            for pile in piles:
                s += (pile-1) // mid + 1
            
            if s <= h:
                r = mid
            else:
                l = mid
            s = 0
        
        for pile in piles:
            s += (pile-1) // l + 1
        if s <= h:
            return l
        return r
        