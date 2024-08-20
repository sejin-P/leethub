class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 1, len(numbers)
        
        while left < right:
            if numbers[left-1]+numbers[right-1] > target:
                right -= 1
            elif numbers[left-1] + numbers[right-1] < target:
                left += 1
            else:
                return [left, right]