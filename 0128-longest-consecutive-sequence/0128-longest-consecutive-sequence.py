class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        endMap = {}
        
        maxLen = 1
        for num in nums:
            if num in endMap:
                continue
            
            lessEnd = endMap.get(num-1)
            moreEnd = endMap.get(num+1)
            if lessEnd is not None and moreEnd is not None:
                endMap[lessEnd] = moreEnd
                endMap[moreEnd] = lessEnd
                endMap[num] = num
                maxLen = max(maxLen, moreEnd-lessEnd+1)
            elif lessEnd is not None:
                endMap[lessEnd] = num
                endMap[num] = lessEnd
                maxLen = max(maxLen, num-lessEnd+1)
            elif moreEnd is not None:
                endMap[moreEnd] = num
                endMap[num] = moreEnd
                maxLen = max(maxLen, moreEnd-num+1)
            else:
                endMap[num] = num
        
        return maxLen
        