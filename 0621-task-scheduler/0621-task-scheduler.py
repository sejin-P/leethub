from collections import defaultdict

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencies = [0]*26
        for task in tasks:
            frequencies[ord(task)-ord('A')] += 1
        
        frequencies.sort()
        
        max_f = frequencies[-1]
        idle = (max_f-1)*(n)
        
        for i in range(24, -1, -1):
            idle -= min(max_f-1, frequencies[i])
        
        return len(tasks) + max(0, idle)
        
            
        