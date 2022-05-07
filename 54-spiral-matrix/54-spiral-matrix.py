class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ver = len(matrix)
        
        if ver == 0:
            return []
        
        hor = len(matrix[0])
        if hor == 0:
            return []
        
        if ver == 1:
            return matrix[0]
        if hor == 1:
            return [arr[0] for arr in matrix]
        
        shell = matrix[0] + [arr[-1] for arr in matrix[1:]] + list(reversed(matrix[-1][0:hor-1])) + [arr[0] for arr in reversed(matrix[1:ver-1])]
        shell += self.spiralOrder([a[1:hor-1] for a in matrix[1:ver-1]])
        return shell
        