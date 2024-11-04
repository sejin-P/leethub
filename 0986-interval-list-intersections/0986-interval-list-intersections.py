class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
    
        res = []
        while i < len(firstList) and j < len(secondList):
            if firstList[i][1] >= secondList[j][0] and firstList[i][0] <= secondList[j][1]:
                res.append([max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])])
            if secondList[j][1] >= firstList[i][1]:
                i += 1
                continue
            if secondList[j][1] < firstList[i][1]:
                j += 1
                continue
    
        return res
        