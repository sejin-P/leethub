from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h = defaultdict(int)
        n = len(nums)
        
        for i in range(n):
            if nums[i] not in h:
                h[nums[i]] = i
            else:
                if i-h[nums[i]] <= k:
                    return True
                else:
                    h[nums[i]] = i
        
        return False
        