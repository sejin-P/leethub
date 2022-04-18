class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        horizon = [{} for _ in range(9)]
        vertical = [{} for _ in range(9)]
        subbox = [[{} for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                number = board[i][j]
                if number == ".":
                    continue
                
                horizon_check = horizon[i].get(number)
                vertical_check = vertical[j].get(number)
                subbox_check = subbox[i//3][j//3].get(number)
                if horizon_check is None and vertical_check is None and subbox_check is None:
                    horizon[i][number] = 1
                    vertical[j][number] = 1
                    subbox[i//3][j//3][number] = 1
                    continue
                return False
        
        return True
        