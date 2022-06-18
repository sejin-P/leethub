class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        square_map = {}
        for i in range(c+1):
            if i ** 2 > c:
                break
            square_map[i**2] = True
        
        for key in square_map.keys():
            if square_map.get(c-key):
                return True
        
        return False
        