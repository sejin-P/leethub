from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.p = [[] for _ in range(numCourses)]

        for pre in prerequisites:
            self.p[pre[0]].append(pre[1])
            
        self.visited = [False]*numCourses
        self.cyclic = [False]*numCourses
        self.res = []
        
        for course in range(numCourses):
            if self.dfs(course):
                return []
        
        return self.res
        
        
    def dfs(self, course):
        if self.visited[course]:
            return False
        if self.cyclic[course]:
            return True
        self.cyclic[course] = True
        for before in self.p[course]:
            if self.dfs(before):
                return True
        
        self.visited[course] = True
        self.res.append(course)
        
        return False
                
            
        
        