class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        prev = [[] for _ in range(n)]
        prev[0] = ["()"]
        
        for i in range(1, n):
            dup = {}
            for j in range((i+1)//2):
                combis1 = prev[j]
                combis2 = prev[i-1-j]
                for combi1 in combis1:
                    for combi2 in combis2:
                        new_combi = combi1+combi2
                        if new_combi not in dup:
                            prev[i].append(new_combi)
                            dup[new_combi] = True
                        new_combi = combi2+combi1
                        if new_combi not in dup:
                            prev[i].append(new_combi)
                            dup[new_combi] = True
            
            for combi in prev[i-1]:
                prev[i].append("("+combi+")")
                
        
        return prev[n-1]
        