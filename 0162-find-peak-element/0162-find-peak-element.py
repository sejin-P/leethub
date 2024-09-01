class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        
        while l < r-1:
            mid = (l+r)//2
            if nums[mid-1] > nums[mid]:
                r = mid - 1
            elif nums[mid+1] > nums[mid]:
                l = mid + 1
            else:
                return mid
    
        return l if nums[r] < nums[l] else r
        