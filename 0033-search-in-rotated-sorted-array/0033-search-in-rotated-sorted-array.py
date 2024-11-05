class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return -1 if nums[0] != target else 0
        
        mid = len(nums)//2
        
        if nums[0] <= target < nums[mid]:
            return self.search(nums[:mid], target)
        if nums[mid] <= target <= nums[-1]:
            res = self.search(nums[mid:], target)
            return -1 if res == -1 else mid + res
        
        if nums[mid] < nums[0]:
            return self.search(nums[:mid], target)
        
        if nums[mid] >= nums[-1]:
            res = self.search(nums[mid:], target)
            return -1 if res == -1 else mid + res
        
        
        return -1