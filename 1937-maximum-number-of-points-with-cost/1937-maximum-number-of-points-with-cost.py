class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(points[0]))] for _ in range(len(points))]
        
        for i in range(len(points[0])):
            dp[0][i] = points[0][i]
        
        for i in range(1, len(points)):
            ldp = [0 for _ in range(len(points[0]))]
            rdp = [0 for _ in range(len(points[0]))]
            for j in range(len(points[0])):
                if j == 0:
                    ldp[j] = dp[i-1][j]
                    rdp[len(points[0])-1-j] = dp[i-1][len(points[0])-1-j]
                    continue
                ldp[j] = max(ldp[j-1]-1, dp[i-1][j])
                rdp[len(points[0])-1-j] = max(rdp[len(points[0])-j]-1, dp[i-1][len(points[0])-j-1])
            
            for j in range(len(points[0])):
                dp[i][j] = points[i][j] + max(ldp[j], rdp[j])
        
        return max(dp[-1])
        