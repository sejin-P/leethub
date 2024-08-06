from collections import deque

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [-1]
        left_arr = deque([])
        right_arr = deque(nums[1:])
        res = []
        
        for i in range(len(nums)):
            found = False
            for j in range(len(right_arr)):
                if right_arr[j] > nums[i]:
                    res.append(right_arr[j])
                    found = True
                    break
            if found:
                left_arr.append(nums[i])
                right_arr.popleft()
                continue
            
            for j in range(len(left_arr)):
                if left_arr[j] > nums[i]:
                    res.append(left_arr[j])
                    found = True
                    break
            
            if not found:
                res.append(-1)
            
            if i == len(nums) - 1:
                return res
                
            left_arr.append(nums[i])
            right_arr.popleft()
            