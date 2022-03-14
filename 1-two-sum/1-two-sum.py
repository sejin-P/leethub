class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i in range(len(nums)):
            reverse = hmap.get(nums[i])
            if reverse != None:
                return [reverse, i]
            hmap[target-nums[i]] = i