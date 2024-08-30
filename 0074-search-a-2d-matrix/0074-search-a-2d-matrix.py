class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        left, right = 0, m-1
        
        while left < right:
            mid = (left+right)//2
            if matrix[left][0] < target and target < matrix[mid][0]:
                right = mid
                continue
                
            if matrix[mid][0] < target and target < matrix[right][0]:
                if left == mid:
                    break
                left = mid 
                continue
                
            if matrix[left][0] > target:
                return False
            
            if matrix[right][0] < target:
                left = right
                
            if matrix[left][0] == target:
                return True
            if matrix[mid][0] == target:
                return True
            if matrix[right][0] == target:
                return True
        
        row = left if matrix[right][0] > target else right
        
        left, right = 0, n-1
        
        while left< right:
            mid = (left+right)//2
            if matrix[row][left] < target and target < matrix[row][mid]:
                right = mid
                continue
                
            if matrix[row][mid] < target and target < matrix[row][right]:
                if left == mid:
                    break
                left = mid 
                continue
                
            if matrix[row][left] > target:
                return False
            
            if matrix[row][right] < target:
                left = right
                
            if matrix[row][left] == target:
                return True
            if matrix[row][mid] == target:
                return True
            if matrix[row][right] == target:
                return True
            
        return matrix[row][left] == target or matrix[row][right] == target