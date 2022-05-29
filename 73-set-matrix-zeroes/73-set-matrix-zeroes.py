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
        
        for key in list(ver_di.keys()):
            matrix[key] = [0 for _ in range(hor)]
        for key in list(hor_di.keys()):
            for i in range(ver):
                matrix[i][key] = 0
        
        return
                
        