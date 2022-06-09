class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[], [nums[0]]]
        nums.sort()
        bundles = []
        
        buffer = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                buffer.append(nums[i])
            else:
                bundles.append(buffer)
                buffer = [nums[i]]
        
        if buffer:
            bundles.append(buffer)
        
        result = [[]]
        for bundle in bundles:
            length = len(result)
            for i in range(length):
                for j in range(1, len(bundle)+1):
                    result += [result[i]+bundle[:j]]
        
        return result
        