from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        self.visited = [False]*n
        self.cyclic = [False]*n
        self.di = defaultdict(list)
        
        for edge in edges:
            self.di[edge[0]].append(edge[1])
            self.di[edge[1]].append(edge[0])
            
        if self.dfs(0, -1):
            return False
        if sum(self.visited) != n:
            return False
        return True
            
    
    def dfs(self, idx, previous):
        if self.visited[idx]:
            return False
        if self.cyclic[idx]:
            return True
        
        self.cyclic[idx] = True
        
        for after in self.di[idx]:
            if after == previous:
                continue
            if self.dfs(after, idx):
                return True
        
        self.visited[idx] = True
        
        return False
        