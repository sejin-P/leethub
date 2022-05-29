class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ver = len(matrix)
        hor = len(matrix[0])
        
        ver_di = {}
        hor_di = {}
        
        for i in range(ver):
            for j in range(hor):
                if matrix[i][j] == 0:
                    ver_di[i] = True
                    hor_di[j] = True
        
        for i in range(ver):
            for j in range(hor):
                if ver_di.get(i) is not None:
                    matrix[i][j] = 0
                elif hor_di.get(j) is not None:
                    matrix[i][j] = 0
        
        return
                
        