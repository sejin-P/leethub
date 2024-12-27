class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        
        parentMap = defaultdict(list)
        for i in range(len(pid)):
            if ppid[i] == 0:
                continue
            parentMap[ppid[i]].append(pid[i])
            
        stack = [kill]
        
        res = []
        while stack:
            process = stack.pop()
            res.append(process)
            for child in parentMap[process]:
                stack.append(child)
        
        return res
        