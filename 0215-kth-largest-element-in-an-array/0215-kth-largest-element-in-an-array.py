class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_val = min(nums)
        max_val = max(nums)
        
        cnts = [0]*(max_val-min_val+1)
        
        for num in nums:
            cnts[num-min_val] += 1
        
        for i in range(len(cnts)-1, -1, -1):
            k -= cnts[i]
            if k <= 0:
                return min_val+i
        
        return -1
        