class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        if n%2 == 0:
            self.evenRotate(matrix, n)
        else:
            self.oddRotate(matrix, n)
        return
    
    def oddRotate(self, matrix: List[List[int]], n: int) -> None:
        end = (n+1)//2
        for i in range(end-1):
            for j in range(end-1):
                first = matrix[i][j]
                second = matrix[j][n-1-i]
                third = matrix[n-1-i][n-1-j]
                fourth = matrix[n-1-j][i]
                matrix[j][n-1-i] = first
                matrix[n-1-i][n-1-j] = second
                matrix[n-1-j][i] = third
                matrix[i][j] = fourth
        for i in range(end-1):
            first = matrix[end-1][i]
            second = matrix[i][n-end]
            third = matrix[n-end][n-1-i]
            fourth = matrix[n-1-i][end-1]
            matrix[i][n-end] = first
            matrix[n-end][n-1-i] = second
            matrix[n-1-i][end-1] = third
            matrix[end-1][i] = fourth
        
    def evenRotate(self, matrix: List[List[int]], n: int) -> None:
        end = (n+1)//2
        for i in range(end):
            for j in range(end):
                first = matrix[i][j]
                second = matrix[j][n-1-i]
                third = matrix[n-1-i][n-1-j]
                fourth = matrix[n-1-j][i]
                matrix[j][n-1-i] = first
                matrix[n-1-i][n-1-j] = second
                matrix[n-1-j][i] = third
                matrix[i][j] = fourth
        return
        
        