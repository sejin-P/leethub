class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1 if nums[0] >= target else 0
        left, right = 0, 0
        s = 0
        res = n+1

        while right < n:
            s += nums[right]
            if s >= target:
                res = min(res, right-left+1)
                while left <= right:
                    s -= nums[left]
                    if s < target:
                        left += 1
                        break
                    else:
                        left += 1
                        res = min(res, right-left+1)
                        
            right += 1
            
                        
        
        return res if res <= n else 0