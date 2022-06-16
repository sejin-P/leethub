class Solution:
    def findDerangement(self, n: int) -> int:
        if n == 1:
            return 0
        if n == 2:
            return 1
        
        lastlast, last = 0,1
        for i in range(3, n+1):
            pres = ((i-1)*(last+lastlast))%(10**9+7)
            lastlast = last
            last = pres
            
            
        return pres
        