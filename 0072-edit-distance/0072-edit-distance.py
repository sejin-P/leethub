class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)
        res = [[0 for _ in range(len(word2))] for _ in range(len(word1))]
        
        met_dup = False
        for i in range(len(word2)):
            if word2[i] == word1[0]:
                met_dup = True
            if met_dup:
                res[0][i] = i
            else:
                res[0][i] = i+1
        
        met_dup = False
        for i in range(len(word1)):
            if word1[i] == word2[0]:
                met_dup = True
            if met_dup:
                res[i][0] = i
            else:
                res[i][0] = i+1
                
        for i in range(1, len(word1)):
            for j in range(1, len(word2)):
                if word1[i] == word2[j]:
                    res[i][j] = res[i-1][j-1]
                else:
                    res[i][j] = min(res[i-1][j-1], res[i-1][j], res[i][j-1])+1
                    
        return res[len(word1)-1][len(word2)-1]