class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        ans, l, r = 0, 0, 0
        min_dq, max_dq = deque(), deque()
        
        while r < len(nums):
            
            while min_dq and nums[min_dq[-1]] >= nums[r]:
                min_dq.pop()
            while max_dq and nums[max_dq[-1]] <= nums[r]:
                max_dq.pop()
            min_dq.append(r)
            max_dq.append(r)
            
            while nums[max_dq[0]] - nums[min_dq[0]] > limit:
                l += 1
                if min_dq[0] < l:
                    min_dq.popleft()
                if max_dq[0] < l:
                    max_dq.popleft()
                    
            ans = max(ans, r - l+1)
            
            r += 1
        
        return ans
        