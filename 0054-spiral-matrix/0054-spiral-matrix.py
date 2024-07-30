class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        height = len(matrix)
        if height == 0:
            return []
        length = len(matrix[0])
        if length == 0:
            return []
        
        if height == 1:
            return matrix[0]
        if length == 1:
            return [arr[0] for arr in matrix]
        
        res = matrix[0] + [arr[-1] for arr in matrix[1:]] + list(reversed(matrix[-1][0:length-1])) + [arr[0] for arr in reversed(matrix[1:height-1])]
        res += self.spiralOrder([a[1:length-1] for a in matrix[1:height-1]])
        return res
        
        