class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        
        if right == 0:
            return 0 if nums[0] == target else -1
        
        while left < right:
            mid = (left+right)//2
            left_val, right_val, mid_val = nums[left], nums[right], nums[mid]
            
            if left_val == target:
                return left
            if right_val == target:
                return right
            if mid_val == target:
                return mid
            
            if mid_val < right_val:
                if mid_val < target and target < right_val:
                    left = mid + 1
                    continue
                right = mid - 1
            else:
                if left_val < target and target < mid_val:
                    right = mid - 1
                    continue
                left = mid + 1
        
        return -1
        