class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = abs(target-nums[0]-nums[1]-nums[-1])
        result = nums[0]+nums[1]+nums[-1]
        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(target-s) < diff:
                    diff = abs(target-s)
                    result = s
                if target < s:
                    r -= 1
                else:
                    l += 1
            
        return result
                