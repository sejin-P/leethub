class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        sub_sum = 0
        cached_mod = {0: -1}
        for i, num in enumerate(nums):
            sub_sum = (sub_sum + num) % k
            idx = cached_mod.get(sub_sum)
            if idx is None:
                cached_mod[sub_sum] = i
            else:
                if i - idx == 1:
                    continue
                else:
                    return True
        
        return False
        