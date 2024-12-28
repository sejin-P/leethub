class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dup = 1
        prev = nums[0]
        removeds = deque([])
        res = 0
        for i, num in enumerate(nums[1:]):
            if num != prev:
                dup = 0
                prev = num
            if dup < 2:
                if removeds:
                    removed = removeds.popleft()
                    nums[removed] = num
                    removeds.append(i+1)
            else:
                removeds.append(i+1)
                res += 1
            dup += 1
        
        return len(nums) - res
 
            
        