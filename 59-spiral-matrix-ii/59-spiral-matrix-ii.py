class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        return self.generateMatrixWithInit(n, 1)
    
    def generateMatrixWithInit(self, n: int, init: int) -> List[List[int]]:
        if n == 1:
            return [[init]]
        if n == 2:
            return [[init, init+1], [init+3, init+2]]
        
        previous = self.generateMatrixWithInit(n-2, init+4*n-4)
        for i in range(n-2):
            previous[i].insert(0, init+4*n-5-i)
            previous[i].append(init+n+i)
        return [[init+i for i in range(n)]] + previous + [[init+3*n-3-i for i in range(n)]]
        