class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque([0])
        for i in range(1, k):
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)
        
        ans = [nums[dq[0]]]
        
        for i in range(k, len(nums)):
            if i - k + 1 > dq[0]:
                dq.popleft()
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)
            ans.append(nums[dq[0]])
        return ans
        