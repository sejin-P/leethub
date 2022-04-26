class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[nums[0]]]
        
        n = len(nums)
        prev = self.permute(nums[1:])
        result = []
        for li in prev:
            result.append([nums[0]]+li)
            for i in range(1, n-1):
                result.append(li[:i]+[nums[0]]+li[i:])
            result.append(li+[nums[0]])
            
        return result
        