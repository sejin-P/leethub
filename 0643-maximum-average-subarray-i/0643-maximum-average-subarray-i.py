class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
    
        n = len(nums)
        s = sum(nums[:k])
        if n == k:
            return s/k
        maxS = s
        for i in range(0, n-k):
            s -= nums[i]
            s += nums[i+k]
            maxS = max(maxS, s)
        
        return maxS/k
        