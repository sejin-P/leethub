class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)
        
        idx = 2
        k = len(nums)
        duplicated = 0
        while idx < k:
            nums[idx] = nums[idx+duplicated]
            if nums[idx-2] == nums[idx-1] and nums[idx-1] == nums[idx]:
                duplicated += 1
                k -= 1
                continue
            idx += 1
        return k