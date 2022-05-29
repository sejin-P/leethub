class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return self.combineWithDict(n, k, {})
        
    def combineWithDict(self, n, k, store):
        if k == 1:
            return [[i] for i in range(1, n+1)]
        if k == n:
            return [[i for i in range(1, n+1)]]
        
        if store.get((n,k)) is not None:
            return store.get((n,k))
        
        first = self.combineWithDict(n-1,k-1,store)
        store[(n-1,k-1)] = first
        
        second = self.combineWithDict(n-1, k, store)
        store[(n-1,k)] = second
        
        return [li+[n] for li in first] + second
        
        
        
        
        