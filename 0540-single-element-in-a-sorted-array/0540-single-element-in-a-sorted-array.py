class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
    
        mid = len(nums)//2

        if nums[mid-1] != nums[mid] and nums[mid] != nums[mid+1]:
            return nums[mid]

        # 대부분 답들은

        if nums[mid-1] == nums[mid]:
            # mid까지 홀수개
            if mid % 2 == 0:
                return self.singleNonDuplicate(nums[:mid+1])
            return self.singleNonDuplicate(nums[mid+1:])
        # mid까지 홀수개
        if mid % 2 == 0:
            return self.singleNonDuplicate(nums[mid:])
        return self.singleNonDuplicate(nums[:mid])