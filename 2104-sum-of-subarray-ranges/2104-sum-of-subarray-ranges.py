class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(n):
            minVal = nums[i]
            maxVal = nums[i]
            for j in range(n-i):
                if minVal > nums[i+j]:
                    minVal = nums[i+j]
                if maxVal < nums[i+j]:
                    maxVal = nums[i+j]
                res += maxVal - minVal
        
        return res
        