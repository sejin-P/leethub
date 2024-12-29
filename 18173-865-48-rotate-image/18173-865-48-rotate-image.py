class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        half = n//2
        for i in range(half):
            for j in range(half):
                matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j], matrix[n-1-j][i] = matrix[n-1-j][i], matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j]
        if n % 2 == 1:
            for i in range(half):
                matrix[half][i], matrix[i][n-1-half], matrix[n-1-half][n-1-i], matrix[n-1-i][half] = matrix[n-1-i][half], matrix[half][i], matrix[i][n-1-half], matrix[n-1-half][n-1-i]
        
        return
        