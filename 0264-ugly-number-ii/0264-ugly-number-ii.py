import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        h = []
        heapq.heappush(h, 1)
        visited = {}
        base = [2,3,5]
        
        current = 1
        for _ in range(n):
            current = heapq.heappop(h)
            
            for p in base:
                num = p*current
                if num not in visited:
                    heapq.heappush(h, num)
                    visited[num] = True
        
        return current
                
        