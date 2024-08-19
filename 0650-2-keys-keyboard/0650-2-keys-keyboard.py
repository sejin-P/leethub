class Solution:
    def minSteps(self, n: int) -> int:
        res = [1000]*(n+1)
        res[1] = 0
        for i in range(2, n+1):
            for j in range(1, i//2+1):
                if i%j==0:
                    res[i] = min(res[i], res[j]+i//j)
                    
        return res[n]
        