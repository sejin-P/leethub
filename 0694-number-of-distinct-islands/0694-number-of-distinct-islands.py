class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        islands = {}
        origins = {}
        
        height = len(grid)
        length = len(grid[0])
        
        for i in range(height):
            for j in range(length):
                if not grid[i][j]:
                    continue
                if i == 0 and j == 0:
                    islands[(i, j)] = [(i, j)]
                    origins[(i, j)] = (i, j)
                    continue
                if j == 0:
                    if grid[i-1][j]:
                        islands[origins[(i-1, j)]].append((i, j))
                        origins[(i, j)] = origins[(i-1, j)]
                    else:
                        islands[(i, j)] = [(i, j)]
                        origins[(i, j)] = (i, j)
                    continue
                if i == 0:
                    if grid[i][j-1]:
                        islands[origins[(i, j-1)]].append((i, j))
                        origins[(i, j)] = origins[(i, j-1)]
                    else:
                        islands[(i, j)] = [(i, j)]
                        origins[(i, j)] = (i, j)
                    continue
                
                if grid[i-1][j] and grid[i][j-1]:
                    if origins[(i-1,j)] != origins[(i, j-1)]:
                        wrongKey = origins[(i, j-1)]
                        for wrongOrigin in islands[origins[(i, j-1)]]:
                            islands[origins[(i-1,j)]].append(wrongOrigin)
                            origins[wrongOrigin] = origins[(i-1,j)]
                        del islands[wrongKey]
                    islands[origins[(i-1,j)]].append((i, j))
                    origins[(i, j)] = origins[(i-1, j)]
                    continue
                
                if grid[i-1][j]:
                    islands[origins[(i-1,j)]].append((i, j))
                    origins[(i, j)] = origins[(i-1, j)]
                    continue
                if grid[i][j-1]:
                    islands[origins[(i,j-1)]].append((i, j))
                    origins[(i, j)] = origins[(i, j-1)]
                    continue
                
                islands[(i,j)] = [(i,j)]
                origins[(i,j)] = (i,j)
        
        distinctIslands = []
        cnt = 0
        for origin, island in islands.items():
            d = []
            for isl in island:
                d.append((isl[0]-origin[0], isl[1]-origin[1]))
            isDistinct = True
            for distinct in distinctIslands:
                isMatched = True
                if len(distinct) != len(d):
                    continue
                for i, isl in enumerate(d):
                    if isl[0] != distinct[i][0] or isl[1] != distinct[i][1]:
                        isMatched = False
                        break
                if isMatched:
                    isDistinct = False
                    break
                        
            if isDistinct:
                distinctIslands.append(d)
                cnt += 1
                
        return cnt
                
        