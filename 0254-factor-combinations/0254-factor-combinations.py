class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []
        def factor(cur, i):
            num = cur.pop()
            while i*i <= num:
                if num%i == 0:
                    div = num//i
                    res.append(cur+[i,div])
                    factor(cur+[i,div], i)
                i += 1
        
        factor([n], 2)
        return res
            
        
        