class Solution:
    def findMaximums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        stack = []
        ris = [n] * n
        lis = [-1] * n
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                ri = stack.pop()
                ris[ri] = i
            if stack:
                lis[i] = stack[-1]
            stack.append(i)
        for i in range(n):
            maxLen = ris[i] - lis[i] - 1
            res[maxLen-1] = max(res[maxLen-1], nums[i])
        for i in range(n-2, -1, -1):
            res[i] = max(res[i], res[i+1])
        
        return res
        
        