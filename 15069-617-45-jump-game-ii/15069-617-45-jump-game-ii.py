class Solution:
    def jump(self, nums: List[int]) -> int:
        idx = 0
        n = len(nums)
        j = 0
        while idx < n-1:
            maxJump = 0
            maxJumpIdx = 0
            for i in range(1, nums[idx]+1):
                if idx+i == n-1:
                    idx = n-1
                    break
                if nums[idx+i]+(idx+i) > maxJump:
                    maxJump = nums[idx+i]+(idx+i)
                    maxJumpIdx = i
            j += 1
            idx += maxJumpIdx
        
        return j
        