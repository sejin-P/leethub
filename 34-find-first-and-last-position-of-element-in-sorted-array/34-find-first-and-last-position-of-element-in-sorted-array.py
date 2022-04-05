class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        
        if len(nums) == 1:
            return [0,0] if nums[0] == target else [-1,-1]
        
        left, right = 0, len(nums)
        result = [-1, -1]
        
        while left < right:
            mid = (left+right) // 2
            if nums[mid] == target:
                right = mid
                result[0], result[1] = mid, mid
            elif nums[mid] < target:
                left = mid +1
            else:
                right = mid
            
        if result[0] == -1:
            return result
            
        left = result[0]+1
        right = len(nums)
        
        while left < right:
            mid = (left+right) // 2
            if nums[mid] == target:
                left = mid + 1
                result[1] = mid
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid
        
        return result
        