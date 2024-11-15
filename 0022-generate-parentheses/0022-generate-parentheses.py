class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        prev = [[] for _ in range(n)]
        prev[0] = ["()"]
        
        for i in range(1, n):
            for j in range(i):
                if i-j-2 < 0:
                    for combi in prev[j]:
                        prev[i].append("("+combi+")")
                    continue
                for combi1 in prev[j]:
                    for combi2 in prev[i-j-2]:
                        prev[i].append("("+combi1+")"+combi2)
            
            for combi in prev[i-1]:
                prev[i].append("()"+combi)
        
        return prev[-1]
        