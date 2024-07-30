class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        dup = {}
        for i, candidate in enumerate(candidates):
            if candidate in dup:
                continue
            dup[candidate] = True
            if target < candidate:
                continue
            elif target == candidate:
                res.append([candidate])
            elif i == len(candidates)-1:
                return res
            else:
                r = self.combinationSum2(candidates[i+1:], target-candidate)
                if len(r) == 0:
                    continue
                for k in r:
                    k.append(candidate)
                    k.sort()
                    if len(res) == 0:
                        res.append(k)
                        continue
                    l = False
                    for re in res:
                        if len(re) == len(k):
                            for i in range(len(re)):
                                if re[i] != k[i]:
                                    l = False
                                    break
                                else:
                                    l = True
                        if l:
                            break
                    if l:
                        continue
                            
                    res.append(k)
        
        return res
    
        